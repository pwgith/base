terraform {
  source = "../../../modules/s3-instance"
}
inputs = {
  bucket_name = "grunty1"
}