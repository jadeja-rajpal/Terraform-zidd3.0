module "app_bucket" {
  source      = "../../modules/secure-bucket"
  bucket_name = "${var.prefix}-prod-app-tf-demo"
}
