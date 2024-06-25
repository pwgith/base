# Define the environment variable
locals {
  environment     = "infra"
  aws_region      = "ap-southeast-2"
  assume_role_arn = "arn:aws:iam::891377349633:role/terragrunt-admin-role"

}
