export stack_name="MyCognitoUserPoolStack"
./script_cleanup.sh $stack_name
# aws cloudformation deploy --stack-name $stack_name --template-file cf_cognito_user_pool.json 
aws cloudformation deploy --stack-name $stack_name --template-file cf_s3_website.json 
