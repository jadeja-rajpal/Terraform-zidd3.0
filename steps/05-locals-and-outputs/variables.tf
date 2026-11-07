variable "students" {
  description = "One file is created for each name in this list"
  type        = list(string)
  default     = ["alice", "bob", "carol"]
}
