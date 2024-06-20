import jsonschema
import json
from helpers.exceptions.server_errors import ServerError, ResponseError, CodeAssumptionError, HealthCheckError
from helpers.exceptions.http_errors import HTTPError, BadRequestError
import logging
import os

class LambdaHandler:
    def load_model_from_file(self, file_name):
        with open(file_name, encoding='utf-8') as json_file:
            return json.load(json_file)

    def __init__(self, event, context, request_model):
        self.response = None
        self.response_model = None

        if event is None:
            raise CodeAssumptionError('event is not defined')
        self.event = event

        if context is None:
            raise CodeAssumptionError('context is not defined')
        self.context = context

        if request_model is None:
            raise CodeAssumptionError('request_model is not defined')
        self.request_model = request_model

        current_dir = os.path.dirname(os.path.abspath(__file__))
        models_dir = os.path.join(current_dir, 'models')
        self.error_response_model = self.load_model_from_file(os.path.join(models_dir, 'error_response_model.json'))
        self.basic_success_response_model = self.load_model_from_file(os.path.join(models_dir, 'basic_success_response_model.json'))
    

    def get_param(self, key):
        return self.event.get(key)

    def get_body(self):
        return self.event.get('body')

    def get_path_param(self, key):
        return self.event.get('pathParameters').get(key)

    def get_query_param(self, key):
        return self.event.get('queryStringParameters').get(key)

    def get_header(self, key):
        return self.event.get('headers').get(key)

    def get_authorizer(self, key):
        return self.event.get('requestContext').get('authorizer').get(key)

    def get_request_id(self):
        return self.context.aws_request_id

    def get_account_id(self):
        return self.context.invoked_function_arn.split(":")[4]

    def get_region(self):
        return self.context.invoked_function_arn.split(":")[3]

    def get_stage(self):
        return self.context.invoked_function_arn.split(":")[6]

    def get_function_name(self):
        return self.context.function_name

    def get_function_version(self):
        return self.context.function_version

    def get_memory_limit_in_mb(self):
        return self.context.memory_limit_in_mb

    def get_remaining_time_in_millis(self):
        return self.context.get_remaining_time_in_millis()

    def get_logger(self):
        return logging.getLogger()

    def set_generic_successful_response(self, status_code, body):
        self.response_model = self.basic_success_response_model

        self.response = {
            'statusCode': status_code,
            'body': json.dumps(body),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }

    def set_successful_response(self, status_code, body, response_model):
        if (response_model is None):
            raise CodeAssumptionError('response_model is not defined')
        self.response_model = response_model

        self.response = {
            'statusCode': status_code,
            'body': json.dumps(body),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }

    def set_error_response(self, status_code, error_message):
        self.response = {
            'statusCode': status_code,
            'body': json.dumps({'error': error_message}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
        self.response_model = self.error_response_model
    
    def check_request(self):
        if self.event is None:
            raise CodeAssumptionError('Event is not defined')
        # Perform validation against the Swagger schema
        # You can use a library like jsonschema to validate the message against the model
        # Here's an example using jsonschema:
        try:
            jsonschema.validate(self.request_model, self.event)
        except jsonschema.ValidationError as e:
            raise BadRequestError(f'Request does not conform to the model: {e}')

    def check_response(self):
        if self.response_model is None:
            raise CodeAssumptionError('Response model is not defined')
        if self.response is None:
            raise CodeAssumptionError('Response is not defined')
        # Perform validation against the Swagger schema
        # You can use a library like jsonschema to validate the message against the model
        # Here's an example using jsonschema:
        try:
            jsonschema.validate(self.response_model, self.response)
        except jsonschema.ValidationError as e:
            raise ResponseError(f'Response does not conform to the model: {e}')
        
    def get_response(self):
        return self.response

    def process_request(self):
        result = False
        try:
            self.check_request()
            self.process_request_implementation()
            self.check_response()
            result = True
        except HTTPError as e:
            self.get_logger().info(f'Lambda HTTP error: {e}')
            self.set_error_response(e.getHTTPReturnCode(), e.getHTTPReturnText())
        except ServerError as e:
            self.get_logger().error(f'Lambda server error: {e}')
            self.set_error_response(e.getHTTPReturnCode(), e.getHTTPReturnText())
        except Exception as e:
            self.get_logger().error(f'Unexpected error: {e}')
            self.set_error_response(500, 'Internal Server Error')
        return(result)
        
    def process_request_implementation(self):
        # Must call the set_succesul_response method on success
        # and raise a LambdaError on failure
        self.set_generic_successful_response(200, {'message': 'process_request_implementation has not been implemented.'})


