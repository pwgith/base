variable "vpc_name" {
  description = "The name to use for the VPC"
  type        = string
}

variable "vpc_availability_zone" {
  description = "The name to use for the VPC availability zone (eg ap-southeast-2)"
  type        = string
  default     = "ap-southeast-2"
}