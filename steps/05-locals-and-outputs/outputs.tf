output "files_created" {
  description = "Names of the students who got a file"
  value       = keys(local_file.student)
}
