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

resource "aws_s3_bucket_versioning" "env" {
  for_each = aws_s3_bucket.env
  bucket   = each.value.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_public_access_block" "env" {
  for_each = aws_s3_bucket.env
  bucket   = each.value.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
