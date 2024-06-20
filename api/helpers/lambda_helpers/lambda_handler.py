import jsonschema
import json
from helpers.exceptions.server_errors import ServerError, ResponseError, CodeAssumptionError
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
        # Perform validation against the Swagger schema
        try:
            jsonschema.validate(self.event, self.request_model)
        except jsonschema.ValidationError as e:
            raise BadRequestError(f'Request does not conform to the model: {e}')

    def check_response(self):
        # Perform validation against the Swagger schema
        try:
            jsonschema.validate(json.loads(self.response["body"]), self.response_model)
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


