output "bucket_names" {
  description = "Names of the buckets Terraform created"
  value       = [for b in aws_s3_bucket.env : b.bucket]
}

output "module_bucket_names" {
  value = [module.logs.bucket_name, module.assets.bucket_name]
}
