import pytest
import json
from api.helpers.lambda_helpers.lambda_handler import LambdaHandler
from api.helpers.exceptions.server_errors import CodeAssumptionError
from api.helpers.exceptions.http_errors import BadRequestError

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

basic_response_model = {
    "type": "object",
    "properties": {
        "key1": {
            "type": "string"
        }
    },
    "required": ["key1"]
}

basic_request = {"key1": "value1", "key2": "value2"}

def test_basic_lambda_handler_success():
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

def test_basic_lambda_handler_server_error():
    event = {
        "key1": "value1",
        "key2": "value2"
    }
    context = {}

    class Failer(LambdaHandler):
        def process_request_implementation(self):
            raise CodeAssumptionError("test")
        
    
    # Test the response of the lambda_handler function
    handler = Failer(event, context, basic_request_model)
    result = handler.process_request()
    assert result is False
    assert handler.get_response() == {"statusCode": 500, "body": json.dumps({"error": "Code assumption broken"}), "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"}}

def test_basic_lambda_handler_http_error():
    event = {
        "key1": "value1",
        "key2": "value2"
    }
    context = {}

    class Failer(LambdaHandler):
        def process_request_implementation(self):
            raise BadRequestError("test")
        
    
    # Test the response of the lambda_handler function
    handler = Failer(event, context, basic_request_model)
    result = handler.process_request()
    assert result is False
    assert handler.get_response() == {"statusCode": 400, "body": json.dumps({"error": "Bad Request"}), "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"}}


def test_basic_lambda_handler_missing_request_field():
    event = {
        "key2": "value2"
    }
    context = {}

        
    
    # Test the response of the lambda_handler function
    handler = LambdaHandler(event, context, basic_request_model)
    result = handler.process_request()
    assert result is False
    assert handler.get_response() == {"statusCode": 400, "body": json.dumps({"error": "Bad Request"}), "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"}}


def test_basic_lambda_handler_plain_exception():
    event = {
        "key1": "value1",
        "key2": "value2"
    }
    context = {}

    class Failer(LambdaHandler):
        def process_request_implementation(self):
            x = 0
            y = 1/x
        
    
    # Test the response of the lambda_handler function
    handler = Failer(event, context, basic_request_model)
    result = handler.process_request()
    assert result is False
    assert handler.get_response() == {"statusCode": 500, "body": json.dumps({"error": "Internal Server Error"}), "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"}}

def test_basic_lambda_handler_no_context():
    event = {
        "key1": "value1",
        "key2": "value2"
    }
    context = {}
    result = False
    # Test the response of the lambda_handler function
    try:
        handler = LambdaHandler(event, None, basic_request_model)
    except CodeAssumptionError as e:
        result = True
    assert result is True

def test_basic_lambda_handler_no_event():
    event = {
        "key1": "value1",
        "key2": "value2"
    }
    context = {}
    result = False
    # Test the response of the lambda_handler function
    try:
        handler = LambdaHandler(None, context, basic_request_model)
    except CodeAssumptionError as e:
        result = True
    assert result is True
    
def test_basic_lambda_handler_no_model():
    event = {
        "key1": "value1",
        "key2": "value2"
    }
    context = {}
    result = False
    # Test the response of the lambda_handler function
    try:
        handler = LambdaHandler(event, context, None)
    except CodeAssumptionError as e:
        result = True
    assert result is True

def test_basic_lambda_handler_custom_response():
    event = {
        "key1": "value1",
        "key2": "value2"
    }
    context = {}

    response = {
        "key1": "value1"
    }

    class Failer(LambdaHandler):
        def process_request_implementation(self):
            self.set_successful_response(200, response, basic_response_model)
    
    # Test the response of the lambda_handler function
    handler = Failer(event, context, basic_request_model)
    result = handler.process_request()
    assert result is True
    assert handler.get_response() == {"statusCode": 200, "body": json.dumps({"key1": "value1"}), "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"}}

def test_basic_lambda_handler_custom_response_error():
    event = {
        "key1": "value1",
        "key2": "value2"
    }
    context = {}

    response = {
        "key2": "value1"
    }

    class CustomResponse(LambdaHandler):
        def process_request_implementation(self):
            self.set_successful_response(200, response, basic_response_model)
    
    # Test the response of the lambda_handler function
    handler = CustomResponse(event, context, basic_request_model)
    result = handler.process_request()
    assert result is False
    assert handler.get_response() == {"statusCode": 500, "body": json.dumps({"error": "Response does not conform to the model"}), "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"}}

def test_basic_lambda_handler_missing_custom_response():
    event = {
        "key1": "value1",
        "key2": "value2"
    }
    context = {}

    response = {
        "key2": "value1"
    }

    class CustomResponseFailNoResponseModel(LambdaHandler):
        def process_request_implementation(self):
            self.set_successful_response(200, response, None)
    
    # Test the response of the lambda_handler function
    handler = CustomResponseFailNoResponseModel(event, context, basic_request_model)
    result = handler.process_request()
    assert result is False
    assert handler.get_response() == {"statusCode": 500, "body": json.dumps({"error": "Code assumption broken"}), "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*"}}
