variable "tf_state_s3_bucket_name" {
  description = "Name of the S3 bucket to store the Terraform state file"
  type        = string
  default     = true
}

variable "tf_state_lock_table_name" {
  description = "Name of the dynamo db table to act as the state lock file"
  type        = string
  default     = true
}
