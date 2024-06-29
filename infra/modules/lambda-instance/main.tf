provider "aws" {
  region = var.aws_region
  assume_role {
    role_arn = var.assume_role_arn
  }

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

resource "aws_iam_role" "lambda_role" {
    name = "${var.lambda_name}-role"

    assume_role_policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "lambda.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
EOF
}

resource "aws_iam_role_policy" "lambda_policy" {
  name = "${var.lambda_name}-policy"
  role = aws_iam_role.lambda_role.id

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Action = "lambda:InvokeFunction",
        Resource = "${aws_lambda_function.my_lambda.arn}"
      }
    ]
  })
}
