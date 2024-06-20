import pytest
import json
from helpers.lambda_helpers.lambda_handler import LambdaHandler

basic_request_model = {
    "type": "object",
    "properties": {
        "key1": {
            "type": "string"
        },
        "key2": {
            "type": "string"
        }
    },
    "required": ["key1", "key2"]
}

basic_request = {"key1": "value1", "key2": "value2"}

def test_basic_lambda_handler():
    event = {
        "key1": "value1",
        "key2": "value2"
    }
    context = {}
    
    # Test the response of the lambda_handler function
    handler = LambdaHandler(event, context, basic_request_model)
    result = handler.process_request()
    assert result is True
    assert handler.get_response() == {"statusCode": 200, "body": json.dumps({"message": "process_request_implementation has not been implemented."}), "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"}}
