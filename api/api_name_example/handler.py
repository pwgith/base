from api.helpers.lambda_helpers.lambda_handler import LambdaHandler

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

def handler(event, context):
    handler = LambdaHandler(event, context, basic_request_model)
    handler.process_request()
    return handler.get_response()
