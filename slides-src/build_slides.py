import os, sys

OUT = sys.argv[1]
TOTAL = 11

MARK = ('<svg width="44" height="44" viewBox="0 0 44 44"><rect x="0" y="0" width="20" height="20" rx="5" fill="#7F77DD"/>'
        '<rect x="24" y="0" width="20" height="20" rx="5" fill="#AFA9EC"/><rect x="12" y="24" width="20" height="20" rx="5" fill="#1D9E75"/></svg>')
IG = ('<svg width="38" height="38" viewBox="0 0 38 38" fill="none" stroke="#4a4560" stroke-width="3"><rect x="3" y="3" width="32" height="32" rx="10"/>'
      '<circle cx="19" cy="19" r="7.5"/><circle cx="28" cy="10" r="1.6" fill="#4a4560" stroke="none"/></svg>')

ARROW_DEFS = ('<defs><marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
              '<path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>')


def shell(n, title, sub, body, js=True):
    h1 = '<h1>' + title + '</h1>' if title else ''
    s = '<div class="sub">' + sub + '</div>' if sub else ''
    return ('<!doctype html><html><head><meta charset="utf-8"><title>Slide ' + str(n) + '</title>'
            '<link rel="stylesheet" href="style.css"></head><body><div class="slide">'
            '<header class="top"><div class="logo">' + MARK + '<span>Terraform in One Shot</span></div>'
            '<div class="handle">' + IG + '<span>@devops_jadeja</span></div></header>'
            + h1 + s + body +
            '<footer><span>DevOps Jadeja</span><span>' + ('%02d' % n) + ' / ' + str(TOTAL) + '</span></footer>'
            '</div>' + ('<script src="lcode.js"></script>' if js else '<script>document.body.dataset.ready="1"</script>') +
            '</body></html>')


def pill(color, title, sub, left, top, width, target, frm='bottom', to='top', **kw):
    extra = ''.join(' data-%s="%s"' % (k, v) for k, v in kw.items())
    return ('<div class="pill %s" style="left:%dpx;top:%dpx;width:%dpx" data-for="%s" data-from="%s" data-to="%s"%s>'
            '<b>%s</b><i>%s</i></div>' % (color, left, top, width, target, frm, to, extra, title, sub))


def win(left, top, width, height, fname, code, size, lh):
    return ('<div class="win" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx"><div class="bar">%s</div>'
            '<pre style="font-size:%dpx;line-height:%dpx">%s</pre></div>' % (left, top, width, height, fname, size, lh, code))


def k(txt, cls, key=None):
    kk = ' data-k="%s"' % key if key else ''
    return '<span class="%s"%s>%s</span>' % (cls, kk, txt)


slides = {}

# ---------------------------------------------------------------- 01 title
body = """
<svg style="position:absolute;left:1290px;top:150px" width="470" height="470" viewBox="0 0 44 44">
<rect x="0" y="0" width="20" height="20" rx="5" fill="#7F77DD"/><rect x="24" y="0" width="20" height="20" rx="5" fill="#AFA9EC"/><rect x="12" y="24" width="20" height="20" rx="5" fill="#1D9E75"/></svg>
<div style="position:absolute;left:80px;top:140px"><span class="tag purple" style="font-size:30px;padding:8px 26px">with DevOps Jadeja</span></div>
<div style="position:absolute;left:80px;top:222px;font-size:158px;font-weight:800;letter-spacing:-4px;line-height:1.0">Terraform</div>
<div style="position:absolute;left:80px;top:384px;font-size:158px;font-weight:800;letter-spacing:-4px;line-height:1.0;color:#6a4fc9">in One Shot</div>
<div style="position:absolute;left:84px;top:588px;font-size:38px;color:#6b6783;font-weight:500">From zero to your first AWS infrastructure in 90 minutes</div>
<div style="position:absolute;left:84px;top:652px;font-size:36px;font-weight:700;color:#16805f">Click less. Code more. Destroy with one command.</div>
"""
steps = [('purple', 'terraform init', 'download providers'), ('teal', 'terraform plan', 'preview the changes'),
         ('coral', 'terraform apply', 'build it'), ('red', 'terraform destroy', 'delete it all')]
cols = {'purple': ('#f1eefe', '#8b7fe0', '#4527a0'), 'teal': ('#e0f7ef', '#2fb58a', '#0b5e45'),
        'coral': ('#fdeee8', '#e2825f', '#8a3416'), 'red': ('#fdebeb', '#e05a5a', '#8a1f1f')}
xs = [80, 540, 1000, 1460]
for (c, cmd, d), x in zip(steps, xs):
    bg, bd, tx = cols[c]
    body += ('<div style="position:absolute;left:%dpx;top:800px;width:380px;height:150px;border-radius:26px;background:%s;border:3px solid %s;color:%s;padding:30px 20px;text-align:center">'
             '<div class="mono" style="font-size:28px;font-weight:700;white-space:nowrap">%s</div><div style="font-size:28px;margin-top:14px;font-weight:500">%s</div></div>' % (x, bg, bd, tx, cmd, d))
for x in [470, 930, 1390]:
    body += '<svg style="position:absolute;left:%dpx;top:850px" width="60" height="50" viewBox="0 0 60 50"><path d="M8 25H48M36 10L50 25L36 40" fill="none" stroke="#8a86a0" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>' % x
slides[1] = shell(1, '', '', body, js=False)

# ---------------------------------------------------------------- 02 why
body = '<div class="card" style="left:80px;top:250px;width:820px;height:640px"></div>'
body += '<div style="position:absolute;left:116px;top:282px"><span class="tag red" style="font-size:30px">Console clicking</span></div>'
rows = ['S3 &rarr; Create bucket &nbsp;<b>dev</b>', 'S3 &rarr; Create bucket &nbsp;<b>stage</b>', 'S3 &rarr; Create bucket &nbsp;<b>prod</b>',
        'Open each one &rarr; turn on versioning &nbsp;<b>&times; 3</b>', 'Open each one &rarr; block public access &nbsp;<b>&times; 3</b>']
for i, r in enumerate(rows):
    y = 365 + i * 82
    body += ('<div style="position:absolute;left:116px;top:%dpx;width:748px;height:64px;border-radius:16px;background:#fdf3f3;border:2px solid #f3cfcf;display:flex;align-items:center;padding:0 22px;font-size:28px;font-weight:500;color:#5c2a2a">'
             '<span style="width:40px;height:40px;border-radius:50%%;background:#e05a5a;color:#fff;font-weight:700;font-size:24px;display:flex;align-items:center;justify-content:center;margin-right:20px">%d</span>%s</div>' % (y, i + 1, r))
body += '<div style="position:absolute;left:116px;top:795px;width:748px;font-size:27px;color:#8a1f1f;font-weight:600;line-height:1.35">Dozens of clicks. Missed a checkbox on prod? Nobody knows. Tomorrow: do it all again in the second account.</div>'

body += '<div class="card" style="left:1020px;top:250px;width:820px;height:640px"></div>'
body += '<div style="position:absolute;left:1056px;top:282px"><span class="tag green" style="font-size:30px">Terraform</span></div>'
code2 = (k('resource', 'kw') + ' ' + k('"aws_s3_bucket"', 'str') + ' ' + k('"env"', 'str') + ' {\n'
         '  ' + k('for_each', 'attr') + ' = toset([' + k('"dev"', 'str') + ', ' + k('"stage"', 'str') + ', ' + k('"prod"', 'str') + '])\n'
         '  ' + k('bucket', 'attr') + '   = ' + k('"${var.prefix}-${each.key}"', 'str') + '\n}')
body += win(1056, 345, 748, 232, 'main.tf', code2, 25, 38).replace('height:232px', 'height:232px')
body += ('<div style="position:absolute;left:1056px;top:600px;width:748px;text-align:center"><svg width="60" height="46" viewBox="0 0 60 46" style="vertical-align:middle"><path d="M30 4V36M16 24L30 38L44 24" fill="none" stroke="#2fb58a" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
         '<span class="mono" style="font-size:30px;font-weight:700;margin-left:14px;color:#0b5e45">terraform apply</span></div>')
for i, nm in enumerate(['dev', 'stage', 'prod']):
    body += ('<div style="position:absolute;left:%dpx;top:670px;width:228px;height:128px;border-radius:20px;background:#e6f6ee;border:3px solid #3ba776;text-align:center;padding-top:22px;color:#0f5a37">'
             '<div style="font-size:32px;font-weight:700">%s</div><div style="font-size:23px;margin-top:6px;font-weight:500">S3 bucket</div><div style="font-size:20px;margin-top:2px;white-space:nowrap">versioned, private</div></div>' % (1056 + i * 260, nm))
body += '<div style="position:absolute;left:1056px;top:826px;width:748px;font-size:27px;color:#0f5a37;font-weight:600;line-height:1.35">Same result every time. Add an item, apply again.</div>'
body += ('<div style="position:absolute;left:915px;top:525px;width:90px;height:90px;border-radius:50%;background:#6a4fc9;color:#fff;font-size:34px;font-weight:800;display:flex;align-items:center;justify-content:center;z-index:5;border:6px solid #faf9fd">VS</div>')
for i, (a, b) in enumerate([('Repeat', 'run the same code'), ('History', 'Git keeps the history'), ('Clean up', 'terraform destroy')]):
    body += ('<div style="position:absolute;left:%dpx;top:918px;width:560px;height:78px;border-radius:20px;background:#fff;border:2px solid #e4e1f2;display:flex;align-items:center;justify-content:center;font-size:25px;font-weight:500;color:#4a4560;white-space:nowrap">'
             '<b style="color:#6a4fc9;margin-right:12px">%s:</b> <span %s>%s</span></div>' % (80 + i * 600, a, 'class="mono" style="font-size:24px"' if i == 2 else '', b))
slides[2] = shell(2, 'Why Terraform?', 'The boss wants 3 S3 buckets: dev, stage, prod. Versioned and private.', body, js=False)

# ---------------------------------------------------------------- 03 anatomy
L, T, W = 480, 480, 960
code = (k('resource', 'kw', 'blk') + ' ' + k('"local_file"', 'str', 'rtype') + ' ' + k('"hello"', 'str', 'nick') + ' ' + k('{', 'pun') + '\n'
        '  ' + k(k('filename', 'attr') + ' ' + k('=', 'pun') + ' ' + k('"hello.txt"', 'str'), 'x', 'a1') + '\n'
        '  ' + k(k('content', 'attr') + '  ' + k('=', 'pun') + ' ' + k('"Hello from Terraform!"', 'str'), 'x', 'a2') + '\n'
        + k('}', 'pun'))
body = win(L, T, W, 344, 'main.tf', code, 38, 60)
body += pill('purple', 'Resource type', 'local = provider, file = kind', 583, 235, 560, 'rtype')
body += pill('purple', 'Block type', 'resource = build this', 300, 350, 380, 'blk')
body += pill('purple', 'Your nickname', 'you choose it', 923, 350, 360, 'nick')
body += pill('teal', 'Arguments', 'the settings', 110, 630, 330, 'a1 a2', frm='right', to='left', padx=14, pady=6)
body += '<div class="bar-note" style="left:360px;top:866px;width:1200px"><b>In plain English</b><span>Create a file called hello.txt with a greeting inside it</span></div>'
slides[3] = shell(3, 'Anatomy of a Terraform block', '', body)

# ---------------------------------------------------------------- 04 loop
body = ''
cards = [('purple', 'terraform init', 'Download the providers', 'Once per project, and again when you add a new provider.'),
         ('teal', 'terraform plan', 'Preview the changes', 'Changes nothing. Always read it before you apply.'),
         ('coral', 'terraform apply', 'Do it', 'Terraform shows the plan again. Type yes to confirm.'),
         ('red', 'terraform destroy', 'Delete everything', 'Removes only what this project created.')]
for (c, cmd, t, d), x in zip(cards, [80, 540, 1000, 1460]):
    bg, bd, tx = cols[c]
    body += ('<div style="position:absolute;left:%dpx;top:270px;width:380px;height:330px;border-radius:28px;background:#fff;border:3px solid %s;overflow:hidden">'
             '<div class="mono" style="background:%s;color:%s;font-size:29px;font-weight:700;padding:22px 20px;text-align:center;border-bottom:3px solid %s">%s</div>'
             '<div style="padding:26px 26px 0;font-size:34px;font-weight:700;color:%s">%s</div>'
             '<div style="padding:12px 26px 0;font-size:26px;color:#4a4560;line-height:1.4;font-weight:500">%s</div></div>' % (x, bd, bg, tx, bd, cmd, tx, t, d))
for x in [468, 928, 1388]:
    body += '<svg style="position:absolute;left:%dpx;top:400px" width="64" height="50" viewBox="0 0 64 50"><path d="M8 25H52M40 10L54 25L40 40" fill="none" stroke="#8a86a0" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>' % x
body += ('<div style="position:absolute;left:540px;top:640px;width:840px;height:76px;border-radius:38px;border:3px dashed #8b7fe0;background:#faf9fd;display:flex;align-items:center;justify-content:center;font-size:27px;font-weight:600;color:#4527a0;white-space:nowrap">'
         '&#8635;&nbsp; Edit code &rarr; plan &rarr; apply. Repeat as often as you like.</div>')
body += '<div style="position:absolute;left:80px;top:766px;font-size:34px;font-weight:700">How to read a plan</div>'
syms = [('+', 'create', '#e6f6ee', '#3ba776', '#0f5a37'), ('~', 'change in place', '#fff4dc', '#e8a93b', '#7a4a05'),
        ('-', 'destroy', '#fdebeb', '#e05a5a', '#8a1f1f'), ('-/+', 'replace it (destroy, then create)', '#fdebeb', '#e05a5a', '#8a1f1f')]
for (sy, tx, bg, bd, ink), x in zip(syms, [80, 540, 1000, 1460]):
    body += ('<div style="position:absolute;left:%dpx;top:830px;width:380px;height:130px;border-radius:24px;background:%s;border:3px solid %s;color:%s;display:flex;align-items:center;gap:22px;padding:0 26px">'
             '<span class="mono" style="font-size:58px;font-weight:700;min-width:96px;text-align:center">%s</span><span style="font-size:25px;font-weight:600;line-height:1.25">%s</span></div>' % (x, bg, bd, ink, sy, tx))
slides[4] = shell(4, 'The Terraform loop', 'Four commands. You will type all of them today.', body, js=False)

# ---------------------------------------------------------------- 05 code vs state vs reality
body = '<svg style="position:absolute;left:0;top:0" width="1920" height="1080" viewBox="0 0 1920 1080">' + ARROW_DEFS
for x1 in [330, 960, 1590]:
    body += '<line x1="%d" y1="640" x2="%d" y2="716" stroke="#8a86a0" stroke-width="4" stroke-dasharray="10 8" marker-end="url(#ar)"/>' % (x1, 960 + (x1 - 960) * 0.28)
body += '</svg>'
icons = {
    'code': '<svg width="150" height="120" viewBox="0 0 150 120"><rect x="14" y="8" width="122" height="104" rx="16" fill="#fff" stroke="#8b7fe0" stroke-width="5"/><text x="75" y="76" text-anchor="middle" font-family="DejaVu Sans Mono" font-size="52" font-weight="700" fill="#4527a0">{ }</text></svg>',
    'state': '<svg width="150" height="120" viewBox="0 0 150 120"><rect x="24" y="8" width="104" height="104" rx="14" fill="#fff" stroke="#2fb58a" stroke-width="5"/><line x1="48" y1="8" x2="48" y2="112" stroke="#2fb58a" stroke-width="5"/><line x1="64" y1="40" x2="114" y2="40" stroke="#2fb58a" stroke-width="5" stroke-linecap="round"/><line x1="64" y1="62" x2="114" y2="62" stroke="#2fb58a" stroke-width="5" stroke-linecap="round"/><line x1="64" y1="84" x2="96" y2="84" stroke="#2fb58a" stroke-width="5" stroke-linecap="round"/></svg>',
    'cloud': '<svg width="150" height="120" viewBox="0 0 150 120"><g fill="#fff" stroke="#e2825f" stroke-width="5"><circle cx="48" cy="72" r="26"/><circle cx="82" cy="50" r="32"/><circle cx="112" cy="74" r="24"/></g><rect x="46" y="62" width="68" height="38" fill="#fff"/><path d="M48 98H112" stroke="#e2825f" stroke-width="5" stroke-linecap="round"/></svg>'}
items = [('purple', 'code', 'Your code', 'what you WANT', 'main.tf files', 80),
         ('teal', 'state', 'The state file', 'what Terraform REMEMBERS', 'terraform.tfstate', 710),
         ('coral', 'cloud', 'Reality', 'what EXISTS now', 'AWS, or your laptop', 1340)]
for c, ic, t, s, d, x in items:
    bg, bd, tx = cols[c]
    body += ('<div style="position:absolute;left:%dpx;top:260px;width:500px;height:380px;border-radius:30px;background:%s;border:3px solid %s;text-align:center;padding-top:34px;color:%s">'
             '%s<div style="font-size:42px;font-weight:700;margin-top:14px">%s</div><div style="font-size:30px;font-weight:600;margin-top:6px">%s</div>'
             '<div class="mono" style="font-size:25px;margin-top:16px;opacity:.85">%s</div></div>' % (x, bg, bd, tx, icons[ic], t, s, d))
body += '<div class="mono" style="position:absolute;left:740px;top:720px;width:440px;height:96px;border-radius:48px;background:#6a4fc9;color:#fff;font-size:38px;font-weight:700;display:flex;align-items:center;justify-content:center">terraform plan</div>'
body += ('<div class="bar-note" style="left:460px;top:846px;width:1000px"><b>The answer</b><span>Here is what I must change so that reality matches your code.</span></div>')
slides[5] = shell(5, 'Code vs state vs reality', 'The big idea of the day: terraform plan compares all three.', body, js=False)

# ---------------------------------------------------------------- 06 variable / locals / output
L, T, W = 480, 235, 930
code = (k('variable', 'kw', 'v') + ' ' + k('"students"', 'str') + ' {\n'
        '  ' + k('type', 'attr') + '    = list(string)\n'
        '  ' + k('default', 'attr') + ' = [' + k('"alice"', 'str') + ', ' + k('"bob"', 'str') + ', ' + k('"carol"', 'str') + ']\n}\n'
        + k('locals', 'kw', 'l') + ' {\n'
        '  ' + k('greeting', 'attr') + ' = ' + k('"Hello"', 'str') + '\n}\n'
        + k('resource', 'kw') + ' ' + k('"local_file"', 'str') + ' ' + k('"student"', 'str') + ' {\n'
        '  ' + k('for_each', 'attr') + ' = toset(' + k('var.students', 'ref', 'vs') + ')\n'
        '  ' + k('filename', 'attr') + ' = ' + k('"${each.key}.txt"', 'str') + '\n'
        '  ' + k('content', 'attr') + '  = ' + k(k('"${', 'str') + k('local.greeting', 'ref') + k('}, ${each.key}!\\n"', 'str'), 'x', 'lr') + '\n}\n'
        + k('output', 'kw', 'o') + ' ' + k('"files_created"', 'str') + ' {\n'
        '  ' + k('value', 'attr') + ' = keys(' + k('local_file.student', 'ref', 'or') + ')\n}')
body = win(L, T, W, 690, 'variables.tf + main.tf + outputs.tf', code, 28, 40)
body += pill('purple', 'variable', 'an input from outside', 40, 285, 400, 'v', frm='right', to='left')
body += pill('teal', 'locals', 'calculated inside', 40, 445, 400, 'l', frm='right', to='left')
body += pill('coral', 'output', 'printed after apply', 40, 765, 400, 'o', frm='right', to='left')
body += pill('purple', 'var.students', 'read an input with var.', 1440, 560, 440, 'vs', frm='left', to='right')
body += pill('teal', 'local.greeting', 'read a local with local. (singular)', 1440, 700, 440, 'lr', frm='left', to='right')
body += pill('coral', 'type.nickname', 'refer to another resource', 1440, 820, 440, 'or', frm='left', to='right')
slides[6] = shell(6, 'variable, locals, output', '', body)

# ---------------------------------------------------------------- 07 s3 for_each
L, T, W = 360, 420, 1200
code = (k('resource', 'kw', 'blk') + ' ' + k('"aws_s3_bucket"', 'str', 'rt') + ' ' + k('"env"', 'str', 'nick') + ' {\n'
        '  ' + k(k('for_each', 'attr') + ' = toset([' + k('"dev"', 'str') + ', ' + k('"stage"', 'str') + ', ' + k('"prod"', 'str') + '])', 'x', 'fe') + '\n'
        '  ' + k('bucket', 'attr') + '   = ' + k('"${var.prefix}-${each.key}-tf-demo"', 'str') + '\n'
        '  ' + k('tags', 'attr') + '     = ' + k('merge', 'ref', 'mg') + '(local.tags, { Environment = ' + k('each.key', 'ref', 'ek') + ' })\n'
        + k('}', 'pun'))
body = win(L, T, W, 364, 'main.tf', code, 32, 52)
body += pill('purple', 'Resource type', 'aws = provider, s3_bucket = kind', 457, 250, 520, 'rt')
body += pill('purple', 'Your nickname', 'you choose it', 1040, 250, 300, 'nick')
body += pill('teal', 'for_each', 'one per list item', 40, 520, 300, 'fe', frm='right', to='left', padx=12)
body += pill('coral', 'merge()', 'combine two tag maps', 500, 840, 400, 'mg', frm='top', to='bottom')
body += pill('teal', 'each.key', 'the current item: dev, stage, prod', 1180, 840, 440, 'ek', frm='top', to='bottom')
slides[7] = shell(7, 'Three buckets from one block', 'for_each: write the resource once, get one copy per item.', body)

# ---------------------------------------------------------------- 08 aws architecture
body = '<svg style="position:absolute;left:0;top:0;z-index:3" width="1920" height="1080" viewBox="0 0 1920 1080">' + ARROW_DEFS
body += '<line x1="430" y1="475" x2="570" y2="475" stroke="#6a4fc9" stroke-width="5" marker-end="url(#ar)"/>'
body += '<line x1="1050" y1="640" x2="1124" y2="704" stroke="#8a86a0" stroke-width="4" marker-end="url(#ar)"/>'
body += '<line x1="1050" y1="815" x2="1124" y2="750" stroke="#8a86a0" stroke-width="4" marker-end="url(#ar)"/>'
body += '<line x1="1494" y1="722" x2="1584" y2="722" stroke="#8a86a0" stroke-width="4" marker-end="url(#ar)"/>'
body += '</svg>'
body += ('<div class="card" style="left:80px;top:350px;width:340px;height:250px;text-align:center;padding-top:36px">'
         '<div style="font-size:34px;font-weight:700">Your laptop</div><div class="mono" style="font-size:27px;margin-top:20px;color:#0b5e45;font-weight:700">terraform apply</div>'
         '<div class="mono" style="font-size:24px;margin-top:14px;color:#6b6783">main.tf</div></div>')
body += '<div style="position:absolute;left:580px;top:250px;width:1260px;height:700px;border-radius:32px;border:3px dashed #8b7fe0;z-index:0"></div>'
body += '<div style="position:absolute;left:610px;top:268px"><span class="tag purple" style="font-size:27px">AWS &middot; ap-south-1</span></div>'
for i, nm in enumerate(['dev', 'stage', 'prod']):
    body += ('<div style="position:absolute;left:%dpx;top:335px;width:360px;height:150px;border-radius:24px;background:#e6f6ee;border:3px solid #3ba776;text-align:center;padding-top:24px;color:#0f5a37;z-index:2">'
             '<div style="font-size:31px;font-weight:700">S3 bucket</div><div class="mono" style="font-size:24px;margin-top:8px">yourname-%s-tf-demo</div>'
             '<div style="font-size:23px;margin-top:8px;font-weight:500">versioned &middot; private</div></div>' % (630 + i * 410, nm))
body += '<div style="position:absolute;left:630px;top:520px;font-size:27px;color:#4a4560;font-weight:600">Terraform works out this order from the references:</div>'
boxes = [('purple', 'data.aws_ami.al2023', 'finds the latest Linux image', 630, 580, 420, 120),
         ('teal', 'aws_security_group.web', 'firewall: allow port 80', 630, 760, 420, 120),
         ('coral', 'aws_instance.web', 'EC2 web server (nginx)', 1130, 660, 360, 125)]
for c, t, s, x, y, w, h in boxes:
    bg, bd, tx = cols[c]
    body += ('<div style="position:absolute;left:%dpx;top:%dpx;width:%dpx;height:%dpx;border-radius:22px;background:%s;border:3px solid %s;color:%s;text-align:center;padding-top:22px;z-index:2">'
             '<div class="mono" style="font-size:25px;font-weight:700">%s</div><div style="font-size:25px;margin-top:10px;font-weight:500">%s</div></div>' % (x, y, w, h, bg, bd, tx, t, s))
body += ('<div style="position:absolute;left:1590px;top:665px;width:220px;height:115px;border-radius:22px;background:#fff;border:3px solid #8a86a0;text-align:center;padding-top:22px;color:#4a4560;z-index:2">'
         '<div class="mono" style="font-size:22px;font-weight:700">output web_url</div><div class="mono" style="font-size:22px;margin-top:10px">http://&lt;ip&gt;</div></div>')
slides[8] = shell(8, 'What we build on AWS', 'Three S3 buckets from for_each, plus an EC2 web server.', body, js=False)

# ---------------------------------------------------------------- 09 remote state
body = '<svg style="position:absolute;left:0;top:0;z-index:3" width="1920" height="1080" viewBox="0 0 1920 1080">' + ARROW_DEFS
body += '<line x1="1296" y1="392" x2="1448" y2="410" stroke="#3ba776" stroke-width="5" marker-end="url(#ar)"/>'
body += '<line x1="1296" y1="500" x2="1448" y2="462" stroke="#3ba776" stroke-width="5" marker-end="url(#ar)"/>'
body += '</svg>'
body += '<div class="card" style="left:80px;top:250px;width:780px;height:360px"></div>'
body += '<div style="position:absolute;left:112px;top:276px"><span class="tag red" style="font-size:28px">Local state</span></div>'
for x, nm in [(120, 'Dev A'), (500, 'Dev B')]:
    body += ('<div style="position:absolute;left:%dpx;top:360px;width:240px;height:150px;border-radius:22px;background:#fdf3f3;border:3px solid #e05a5a;text-align:center;padding-top:26px;color:#5c2a2a">'
             '<div style="font-size:32px;font-weight:700">%s</div><div class="mono" style="font-size:22px;margin-top:14px">terraform.tfstate</div><div style="font-size:21px;margin-top:6px">own copy</div></div>' % (x, nm))
body += '<div style="position:absolute;left:376px;top:392px;font-size:80px;font-weight:800;color:#e05a5a;width:110px;text-align:center">&ne;</div>'
body += '<div style="position:absolute;left:112px;top:556px;width:716px;text-align:center;font-size:27px;font-weight:600;color:#8a1f1f">Two notebooks that disagree about what exists.</div>'
body += '<div class="card" style="left:1060px;top:250px;width:780px;height:360px"></div>'
body += '<div style="position:absolute;left:1092px;top:276px"><span class="tag green" style="font-size:28px">Remote state (S3)</span></div>'
for y, nm in [(350, 'Dev A'), (460, 'Dev B')]:
    body += ('<div style="position:absolute;left:1100px;top:%dpx;width:196px;height:84px;border-radius:20px;background:#fff;border:3px solid #3ba776;text-align:center;padding-top:22px;font-size:30px;font-weight:700;color:#0f5a37">%s</div>' % (y, nm))
body += ('<div style="position:absolute;left:1450px;top:330px;width:350px;height:200px;border-radius:24px;background:#e6f6ee;border:3px solid #3ba776;text-align:center;padding-top:22px;color:#0f5a37">'
         '<div style="font-size:32px;font-weight:700">S3 bucket</div><div class="mono" style="font-size:22px;margin-top:12px">dev/terraform.tfstate</div>'
         '<div style="display:inline-block;margin-top:14px;background:#0f5a37;color:#fff;border-radius:999px;padding:8px 22px;font-size:24px;font-weight:700">lock: one at a time</div></div>')
body += '<div style="position:absolute;left:1092px;top:556px;width:716px;text-align:center;font-size:27px;font-weight:600;color:#0f5a37">One shared notebook, with a lock.</div>'
code = ('  ' + k('backend', 'kw') + ' ' + k('"s3"', 'str') + ' {\n'
        '    ' + k('bucket', 'attr') + '       = ' + k('"yourname-terraform-state"', 'str') + '\n'
        '    ' + k('key', 'attr') + '          = ' + k('"dev/terraform.tfstate"', 'str') + '\n'
        '    ' + k('use_lockfile', 'attr') + ' = ' + k('true', 'num') + '\n  }')
body += win(80, 650, 1000, 304, 'backend.tf', code, 28, 40)
notes = [('The bucket must exist first', 'create it separately (bootstrap)'), ('key = one state file per environment', 'dev/..., prod/...'), ('use_lockfile needs Terraform 1.10+', 'older setups used a DynamoDB table')]
for i, (a, b) in enumerate(notes):
    body += ('<div style="position:absolute;left:1130px;top:%dpx;width:710px;height:88px;border-radius:20px;background:#fff;border:2px solid #e4e1f2;padding:14px 26px">'
             '<div style="font-size:27px;font-weight:700;color:#4527a0">%s</div><div style="font-size:23px;color:#6b6783;margin-top:4px;font-weight:500">%s</div></div>' % (650 + i * 108, a, b))
slides[9] = shell(9, 'Remote state with locking', 'Why teams keep state in S3 instead of on laptops.', body, js=False)

# ---------------------------------------------------------------- 10 modules
tree = ('work/\n'
        '\u251c\u2500\u2500 main.tf\n'
        '\u251c\u2500\u2500 modules.tf          ' + k('\u2190 uses it', 'cm') + '\n'
        '\u2514\u2500\u2500 modules/\n'
        '    \u2514\u2500\u2500 secure-bucket/  ' + k('\u2190 written once', 'cm') + '\n'
        '        \u251c\u2500\u2500 main.tf\n'
        '        \u251c\u2500\u2500 variables.tf\n'
        '        \u2514\u2500\u2500 outputs.tf')
body = win(80, 270, 800, 472, 'folders', tree, 30, 46)
code = (k('module', 'kw', 'm') + ' ' + k('"logs"', 'str') + ' {\n'
        '  ' + k('source', 'attr') + '      = ' + k('"./modules/secure-bucket"', 'str', 'src') + '\n'
        '  ' + k('bucket_name', 'attr') + ' = ' + k('"${var.prefix}-logs-tf-demo"', 'str') + '\n}\n'
        + k('module', 'kw') + ' ' + k('"assets"', 'str') + ' {\n'
        '  ' + k('source', 'attr') + '      = ' + k('"./modules/secure-bucket"', 'str') + '\n'
        '  ' + k('bucket_name', 'attr') + ' = ' + k('"${var.prefix}-assets-tf-demo"', 'str', 'bn2') + '\n}')
body += win(960, 400, 880, 440, 'modules.tf', code, 28, 42)
body += pill('purple', 'module block', 'call a reusable module', 960, 270, 360, 'm', frm='bottom', to='top')
body += pill('teal', 'source', 'where the module lives', 1380, 270, 400, 'src', frm='bottom', to='top')
body += pill('coral', 'bucket_name', 'an input: a different value per call', 1130, 890, 640, 'bn2', frm='top', to='bottom')
body += ('<div class="bar-note" style="left:80px;top:790px;width:800px;padding:18px 24px"><b>Same recipe, two buckets</b><span>Fix the module once and both buckets change.</span></div>')
slides[10] = shell(10, 'Modules: write once, reuse everywhere', '', body)


# ---------------------------------------------------------------- 11 environments
tree = ('work/\n'
        '\u251c\u2500\u2500 modules/\n'
        '\u2502   \u2514\u2500\u2500 secure-bucket/   ' + k('\u2190 written once', 'cm') + '\n'
        '\u2514\u2500\u2500 environments/\n'
        '    \u251c\u2500\u2500 dev/     ' + k('\u2190 state: dev/terraform.tfstate', 'cm') + '\n'
        '    \u251c\u2500\u2500 stage/   ' + k('\u2190 state: stage/terraform.tfstate', 'cm') + '\n'
        '    \u2514\u2500\u2500 prod/    ' + k('\u2190 state: prod/terraform.tfstate', 'cm'))
body = win(80, 270, 930, 398, 'folders', tree, 24, 42)
code = (k('module', 'kw', 'm') + ' ' + k('"app_bucket"', 'str') + ' {\n'
        '  ' + k('source', 'attr') + '      = ' + k('"../../modules/secure-bucket"', 'str', 'src') + '\n'
        '  ' + k('bucket_name', 'attr') + ' = ' + k('"jadeja-dev-app-tf-demo"', 'str', 'bn') + '\n'
        + k('}', 'pun'))
body += win(1060, 440, 780, 264, 'dev/main.tf', code, 25, 40)
body += pill('teal', 'source', 'up two folders, into modules', 1360, 280, 480, 'src', frm='bottom', to='top')
body += pill('coral', 'bucket_name', 'a different name per environment', 1260, 770, 580, 'bn', frm='top', to='bottom')
body += ('<div class="bar-note" style="left:80px;top:740px;width:930px;padding:18px 24px"><b>Same module, three folders, three state files</b><span>Destroy dev, and prod is untouched.</span></div>')
slides[11] = shell(11, 'One module, three environments', 'Each folder has its own state, so a change in dev cannot touch prod.', body)

os.makedirs(OUT, exist_ok=True)
names = {1: '01-title', 2: '02-why-terraform', 3: '03-block-anatomy', 4: '04-the-loop', 5: '05-code-state-reality',
         6: '06-variable-locals-output', 7: '07-s3-for-each', 8: '08-aws-architecture', 9: '09-remote-state', 10: '10-modules', 11: '11-environments'}
for n, html in slides.items():
    with open(os.path.join(OUT, names[n] + '.html'), 'w') as f:
        f.write(html)
print('wrote', len(slides), 'slides')
