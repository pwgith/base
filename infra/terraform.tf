terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "~> 5.10.0"
    }
  }

  backend "s3" {
    bucket = "tf-remote-state-base"
    key = "state"
    region = "ap-southeast-2"
    dynamodb_table = "tf-remote-state-base"
  }
}