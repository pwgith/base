terraform {
  source = "../../../modules/dynamodb-instance"
}
inputs = {
  table_name = "trial"
}