provider "aws" {
  region = var.aws_region
  assume_role {
    role_arn = var.assume_role_arn
  }
}

resource "aws_s3_bucket" "basic_s3_bucket" {
  bucket = var.bucket_name
}