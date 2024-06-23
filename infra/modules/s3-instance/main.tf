provider "aws" {
  region = var.aws_region
}

resource "aws_s3_bucket" "basic_s3_bucket" {
  bucket = var.bucket_name
}