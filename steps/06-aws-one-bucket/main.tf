resource "aws_s3_bucket" "demo" {
  bucket        = "${var.prefix}-demo-tf"
  force_destroy = true # demo only: lets destroy delete a bucket that has files in it
}
