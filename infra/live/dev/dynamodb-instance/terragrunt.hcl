locals {
  # Automatically load environment-level variables
  environment_vars = read_terragrunt_config(find_in_parent_folders("env.hcl"))

  # Extract out common variables for reuse
  env_name = local.environment_vars.locals.environment
  aws_region = local.environment_vars.locals.aws_region
}

terraform {
  source = "../../../modules/dynamodb-instance"
}

inputs = {
  table_name = "${local.env_name}-trial-ddb"
  aws_region     = local.aws_region
}