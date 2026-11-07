#!/usr/bin/env bash
# Creates environments/dev, environments/stage and environments/prod.
# Run it from inside work/ like this (use your own two values):
#
#   PREFIX=jadeja STATE_BUCKET=jadeja-terraform-state bash ../steps/12-environments/create-environments.sh
#
set -euo pipefail

PREFIX="${PREFIX:?Set PREFIX, e.g. PREFIX=jadeja}"
STATE_BUCKET="${STATE_BUCKET:?Set STATE_BUCKET, e.g. STATE_BUCKET=jadeja-terraform-state}"

# The module is written once. Reuse the one from step 11, or fetch it from the steps folder.
if [ ! -d modules/secure-bucket ]; then
  cp -r ../steps/11-modules/modules .
fi

for env in dev stage prod; do
  d="environments/$env"
  mkdir -p "$d"

  cat > "$d/providers.tf" <<EOF
terraform {
  required_version = ">= 1.10"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = var.region
}
EOF

  cat > "$d/variables.tf" <<EOF
variable "region" {
  description = "AWS region to build in"
  type        = string
  default     = "ap-south-1"
}

variable "prefix" {
  description = "Your name in lowercase. Used in every bucket name"
  type        = string
}
EOF

  cat > "$d/terraform.tfvars" <<EOF
prefix = "$PREFIX"
EOF

  cat > "$d/backend.tf" <<EOF
terraform {
  backend "s3" {
    bucket       = "$STATE_BUCKET"
    key          = "$env/terraform.tfstate"
    region       = "ap-south-1"
    encrypt      = true
    use_lockfile = true
  }
}
EOF

  cat > "$d/main.tf" <<EOF
module "app_bucket" {
  source      = "../../modules/secure-bucket"
  bucket_name = "\${var.prefix}-$env-app-tf-demo"
}
EOF

  cat > "$d/outputs.tf" <<EOF
output "bucket_name" {
  value = module.app_bucket.bucket_name
}
EOF
done

echo "Created: environments/dev  environments/stage  environments/prod"
