terraform {
  source = "../../../modules/cognito-instance"
}
inputs = {
  user_pool_name = "agw1"
}