resource "aws_lambda_function" "my_lambda" {
    function_name = var.lambda_name
    runtime = "python3.8"  # Replace with your desired runtime
    handler = var.lambda_handler  

    role = aws_iam_role.lambda_role.arn  # Replace with the ARN of your IAM role

    # Replace with your desired Lambda function code
    filename = "lambda_function.zip"
    source_code_hash = filebase64sha256("lambda_function.zip")
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