include {
  path = find_in_parent_folders()
}

dependencies {
  paths = ["../lambda-api_name_example-instance"]
}

dependency "my_lambda" {
  config_path = "../lambda-api_name_example-instance"
  mock_outputs = {
    lambda_invoke_arn = "mock-invoke-arn"
  }
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
  source = "../../../modules/api-gateway-instance"
}



inputs = {
  aws_region                 = local.aws_region
  assume_role_arn            = local.assume_role_arn
  api_integration_invoke_arn = dependency.my_lambda.outputs.lambda_invoke_arn
}


