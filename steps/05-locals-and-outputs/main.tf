locals {
  greeting = "Hello"
}

resource "local_file" "student" {
  for_each = toset(var.students)
  filename = "${each.key}.txt"
  content  = "${local.greeting}, ${each.key}!\n"
}
