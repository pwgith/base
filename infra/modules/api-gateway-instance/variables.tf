variable "aws_region" {
  description = "The AWS region to deploy into"
  type        = string
}

variable "assume_role_arn" {
  description = "The role to use to deploy with"
  type        = string
}

variable "api_integration_invoke_arn" {
  description = "The arn of the lambda invocation to integrate to"
  type        = string
}

variable "lambda_function_name" {
  description = "The name of the lambda function to integrate with"
  type        = string
}
