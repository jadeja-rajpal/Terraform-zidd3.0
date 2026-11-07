# The same recipe (bucket + versioning + private) used twice.
module "logs" {
  source      = "./modules/secure-bucket"
  bucket_name = "${var.prefix}-logs-tf-demo"
}

module "assets" {
  source      = "./modules/secure-bucket"
  bucket_name = "${var.prefix}-assets-tf-demo"
}
