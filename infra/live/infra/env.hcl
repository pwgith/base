# Define the environment variable
locals {
  environment = "infra"
  aws_region  = "ap-southeast-2"
}
inputs {
  tf_state_s3_bucket_name  = "tf-remote-state-base-${local.environment}"
  tf_state_lock_table_name = "tf-remote-state-base-${local.environment}"
}
