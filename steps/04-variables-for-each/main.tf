resource "local_file" "student" {
  for_each = toset(var.students)
  filename = "${each.key}.txt"
  content  = "Hello, ${each.key}!\n"
}
