locals {
  # Automatically load environment-level variables
  environment_vars = read_terragrunt_config(find_in_parent_folders("env.hcl"))

  # Extract out common variables for reuse
  env_name = local.environment_vars.locals.environment
}

terraform {
  source = "../../../modules/vpc-instance"
}


inputs = {
  vpc_name = "${local.env_name}-trial-vpc"
}