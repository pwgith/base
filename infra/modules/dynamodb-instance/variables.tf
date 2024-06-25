variable "aws_region" {
  description = "The AWS region to deploy into"
  type        = string
}

variable "assume_role_arn" {
  description = "The role to use to deploy with"
  type        = string
}

variable "table_name" {
  description = "The name to use for the instance"
  type        = string
}