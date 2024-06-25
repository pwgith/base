include {
  path = find_in_parent_folders()
}

locals {
  # Automatically load environment-level variables
  environment_vars = read_terragrunt_config(find_in_parent_folders("env.hcl"))

  # Extract out common variables for reuse
  env_name        = local.environment_vars.locals.environment
  aws_region      = local.environment_vars.locals.aws_region
  assume_role_arn = local.environment_vars.locals.assume_role_arn
}

terraform {
  source = "../../../modules/lambda-instance"
}

inputs = {
  lambda_name     = "${local.env_name}-api_name_example"
  aws_region      = local.aws_region
  assume_role_arn = local.assume_role_arn
  lambda_handler  = "api/api_name_example/handler.handler"
  lambda_zip_path = "infra/live/dev/lambda-api_name_example-instance/lambda-api_name_example-instance.zip"
  lambda_zip_name = "lambda-api_name_example-instance.zip"
}
