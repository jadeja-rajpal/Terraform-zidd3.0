variable "region" {
  description = "AWS region to build in"
  type        = string
  default     = "ap-south-1"
}

variable "prefix" {
  description = "Your name in lowercase. Used in every bucket name"
  type        = string
}

variable "environments" {
  description = "One bucket is created for each environment name"
  type        = list(string)
  default     = ["dev", "stage", "prod"]
}
