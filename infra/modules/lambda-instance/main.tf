provider "aws" {
  region = var.aws_region
  assume_role {
    role_arn = var.assume_role_arn
  }

}

resource "aws_iam_role" "lambda_role" {
  name = "lambda_execution_role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect    = "Allow",
      Principal = { Service = "lambda.amazonaws.com" },
      Action    = "sts:AssumeRole"
    }]
  })

  // Attach policies as needed
  // e.g., CloudWatch Logs
  // Assume more policies as needed
}


resource "aws_lambda_function" "my_lambda" {
    function_name = var.lambda_name
    runtime = "python3.11"  # Replace with your desired runtime
    handler = var.lambda_handler  
    role = aws_iam_role.lambda_role.arn  # Replace with the ARN of your IAM role


    # Replace with your desired Lambda function code
    filename = var.lambda_zip_name
    source_code_hash = filebase64sha256(var.lambda_zip_name)

    environment {
        variables = {
            PYTHONPATH = "/var/task/api:/var/task"
            LOG_LEVEL  = "WARNING"
        }
    }
}




# resource "aws_lambda_function" "example_lambda" {
#   function_name = var.lambda_function_name
#   runtime       = "python3.9"
#   role          = aws_iam_role.lambda_role.arn
#   handler       = "main.lambda_handler"
#   filename      = "my-deployment-package.zip"
#   depends_on = [
#     aws_iam_role_policy_attachment.lambda_logs,
#     aws_cloudwatch_log_group.example,
#   ]
# }
# resource "aws_cloudwatch_log_group" "example" {
#   name              = "/aws/lambda/${var.lambda_function_name}"
#   retention_in_days = 14
# }
# resource "aws_iam_policy" "lambda_logging" {
#   name        = "lambda_logging"
#   path        = "/"
#   description = "IAM policy for logging from a lambda"
#   policy = <<EOF
# {
#   "Version": "2012-10-17",
#   "Statement": [
#     {
#       "Action": [
#         "logs:CreateLogGroup",
#         "logs:CreateLogStream",
#         "logs:PutLogEvents"
#       ],
#       "Resource": "arn:aws:logs:*:*:*",
#       "Effect": "Allow"
#     }
#   ]
# }
# EOF
# }
# resource "aws_iam_role_policy_attachment" "lambda_logs" {
#   role       = aws_iam_role.lambda_role.name
#   policy_arn = aws_iam_policy.lambda_logging.arn
# }
# resource "aws_iam_role" "lambda_role" {
#   name               = "lambda_role"
#   assume_role_policy = <<EOF
# {
#   "Version": "2012-10-17",
#   "Statement": [
#     {
#       "Action": "sts:AssumeRole",
#       "Principal": {
#         "Service": "lambda.amazonaws.com"
#       },
#       "Effect": "Allow",
#       "Sid": ""
#     }
#   ]
# }
# EOF
# }
