variable "aws_region" {
  description = "The AWS region to deploy into"
  type        = string
}

variable "assume_role_arn" {
  description = "The role to use to deploy with"
  type        = string
}

variable "lambda_name" {
  description = "The name to use for the lambda"
  type        = string
}

variable "lambda_handler" {
  description = "The name to use for the lambda handler (module.function)"
  type        = string
}

variable "lambda_zip_path" {
  description = "The partial path and name of the zip file to be sent to AWS"
  type        = string
}

variable "lambda_zip_name" {
  description = "The name of the zip file to be sent to AWS"
  type        = string
}
