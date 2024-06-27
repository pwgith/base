# API Gateway
provider "aws" {
  region = var.aws_region
  assume_role {
    role_arn = var.assume_role_arn
  }
}

# Create API Gateway REST API
resource "aws_api_gateway_rest_api" "example_api" {
  name        = "example-api"
  description = "Example API Gateway"
}

# Create a Resource
resource "aws_api_gateway_resource" "example_resource" {
  rest_api_id = aws_api_gateway_rest_api.example_api.id
  parent_id   = aws_api_gateway_rest_api.example_api.root_resource_id
  path_part   = "items"
}

# Create GET Method
resource "aws_api_gateway_method" "example_method" {
  rest_api_id   = aws_api_gateway_rest_api.example_api.id
  resource_id   = aws_api_gateway_resource.example_resource.id
  http_method   = "GET"
  authorization = "NONE"
}

# Create Integration
resource "aws_api_gateway_integration" "example_integration" {
  rest_api_id             = aws_api_gateway_rest_api.example_api.id
  resource_id             = aws_api_gateway_resource.example_resource.id
  http_method             = aws_api_gateway_method.example_method.http_method
  integration_http_method = "GET"
  type                    = "AWS_PROXY"
  uri                     = var.lambda_arn

  request_templates = {
    "application/json" = "{\"statusCode\": 200}"
  }
}

# Create Method Response
resource "aws_api_gateway_method_response" "example_response_200" {
  rest_api_id = aws_api_gateway_rest_api.example_api.id
  resource_id = aws_api_gateway_resource.example_resource.id
  http_method = aws_api_gateway_method.example_method.http_method
  status_code = "200"

  response_models = {
    "application/json" = "Empty"
  }
}

# Create Integration Response
resource "aws_api_gateway_integration_response" "example_integration_response_200" {
  rest_api_id = aws_api_gateway_rest_api.example_api.id
  resource_id = aws_api_gateway_resource.example_resource.id
  http_method = aws_api_gateway_method.example_method.http_method
  status_code = aws_api_gateway_method_response.example_response_200.status_code

  response_templates = {
    "application/json" = ""
  }
  
}

# Deploy the API
resource "aws_api_gateway_deployment" "example_deployment" {
  depends_on = [
    aws_api_gateway_integration.example_integration,
    aws_api_gateway_method_response.example_response_200,
    aws_api_gateway_integration_response.example_integration_response_200,
  ]

  rest_api_id = aws_api_gateway_rest_api.example_api.id
  stage_name  = "dev"
}
