sudo apt-get update 
sudo apt-get install unzip curl -y 
curl 'https://d1vvhvl2y92vvt.cloudfront.net/awscli-exe-linux-x86_64.zip' -o 'awscliv2.zip'
unzip -o awscliv2.zip
rm awscliv2.zip
sudo ./aws/install 
curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
sudo apt-add-repository 'deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main'
sudo apt-get update
sudo apt-get install -y gnupg software-properties-common curl
curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
sudo apt-get update
sudo apt-get install terraform -y
wget https://github.com/gruntwork-io/terragrunt/releases/download/v0.58.0/terragrunt_linux_amd64
chmod +x terragrunt_linux_amd64
sudo mv terragrunt_linux_amd64 /usr/local/bin/terragrunt
