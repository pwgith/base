generate "backend" {
  path      = "backend.tf"
  if_exists = "overwrite_terragrunt"
  contents = <<EOF
terraform {
  backend "s3" {
    bucket         = "tf-remote-state-base"
    key            = "infra/${path_relative_to_include()}/terraform.tfstate"
    region         = "ap-southeast-2"
    encrypt        = false
    dynamodb_table = "tf-remote-state-base"
  }
}
EOF
}