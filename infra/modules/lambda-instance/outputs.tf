# Output the Lambda ARN
output "lambda_arn" {
  value = aws_lambda_function.my_lambda.arn
}

output "invoke_arn" {
  value = aws_lambda_function.my_lambda.invoke_arn
}