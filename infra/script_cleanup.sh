status=$(aws cloudformation describe-stacks --stack-name $1 --query Stacks[0].StackStatus --output text || true 2>/dev/null)
echo "Status of stack $1: $status"
if [ "$status" == "ROLLBACK_COMPLETE" ]; then
  aws cloudformation delete-stack --stack-name $1
  echo "Deleted stack $1"
fi