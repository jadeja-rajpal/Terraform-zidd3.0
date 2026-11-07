module "app_bucket" {
  source      = "../../modules/secure-bucket"
  bucket_name = "${var.prefix}-stage-app-tf-demo"
}
