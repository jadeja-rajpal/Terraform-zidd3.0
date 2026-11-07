import sys, glob, os
from playwright.sync_api import sync_playwright

src, out = sys.argv[1], sys.argv[2]
only = sys.argv[3:]
os.makedirs(out, exist_ok=True)
files = sorted(glob.glob(os.path.join(src, '*.html')))
if only:
    files = [f for f in files if any(o in os.path.basename(f) for o in only)]
with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--no-sandbox', '--font-render-hinting=none'])
    pg = b.new_page(viewport={'width': 1920, 'height': 1080}, device_scale_factor=1)
    for f in files:
        pg.on('console', lambda m, f=f: print(os.path.basename(f), 'console:', m.text) if m.type in ('error', 'warning') else None)
        pg.goto('file://' + os.path.abspath(f))
        pg.wait_for_selector('body[data-ready="1"]', timeout=15000)
        pg.wait_for_timeout(200)
        name = os.path.splitext(os.path.basename(f))[0] + '.png'
        pg.screenshot(path=os.path.join(out, name))
        print('rendered', name)
    b.close()
