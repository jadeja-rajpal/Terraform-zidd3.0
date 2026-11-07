resource "local_file" "hello" {
  filename = "hello.txt"
  content  = "Hello from Terraform, version 2!\n"
}
