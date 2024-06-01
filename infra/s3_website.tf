resource "aws_s3_bucket" "basic_s3_bucket" {
  bucket = "my-tf-test-bucket-pw"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}
