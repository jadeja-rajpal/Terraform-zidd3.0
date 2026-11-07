# A backend block cannot use variables, so these values are typed in directly.
# Create the bucket first (see the guide), then run: terraform init -migrate-state
terraform {
  backend "s3" {
    bucket       = "yourname-terraform-state" # CHANGE THIS: your own state bucket
    key          = "dev/terraform.tfstate"
    region       = "ap-south-1"
    encrypt      = true
    use_lockfile = true # native S3 locking, needs Terraform 1.10 or newer
  }
}
