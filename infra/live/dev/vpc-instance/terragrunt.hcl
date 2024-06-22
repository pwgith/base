terraform {
  source = "../../../modules/vpc-instance"
}
inputs = {
  vpc_name = "trial-vpc"
}