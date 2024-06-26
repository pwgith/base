variable "aws_region" {
  description = "The AWS region to deploy into"
  type        = string
}

variable "assume_role_arn" {
  description = "The role to use to deploy with"
  type        = string
}

variable "lambda_arn" {
  description = "The arn of the lambda to integrate to"
  type        = string
}
