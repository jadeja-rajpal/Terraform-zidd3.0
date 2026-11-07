locals {
  tags = {
    Project   = var.prefix
    ManagedBy = "terraform"
  }
}

resource "aws_s3_bucket" "env" {
  for_each      = toset(var.environments)
  bucket        = "${var.prefix}-${each.key}-tf-demo"
  force_destroy = true
  tags          = merge(local.tags, { Environment = each.key })
}
