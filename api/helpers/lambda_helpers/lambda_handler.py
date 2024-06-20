import jsonschema
import json
from helpers.exceptions.server_errors import ServerError, ResponseError, CodeAssumptionError
from helpers.exceptions.http_errors import HTTPError, BadRequestError
import logging
import os
from helpers.log_helpers.log_helper import prepare_log_string
from helpers.log_helpers.method_logger import MethodLogger

module_logger = logging.getLogger(__name__)

class LambdaHandler:
    def load_model_from_file(self, file_name):
        with MethodLogger(module_logger, 'load_model_from_file'):
            with open(file_name, encoding='utf-8') as json_file:
                return json.load(json_file)

    def __init__(self, event, context, request_model):
        with MethodLogger(module_logger, '__init__'):
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
        with MethodLogger(module_logger, 'get_logger'):
            return logging.getLogger()

    def set_generic_successful_response(self, status_code, body):
        with MethodLogger(module_logger, 'set_generic_successful_response'):
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
        with MethodLogger(module_logger, 'set_successful_response'):
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
        with MethodLogger(module_logger, 'set_error_response'):
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
        with MethodLogger(module_logger, 'check_request'):
            # Perform validation against the Swagger schema
            try:
                jsonschema.validate(self.event, self.request_model)
            except jsonschema.ValidationError as e:
                raise BadRequestError(f'Request does not conform to the model: {e}')

    def check_response(self):
        with MethodLogger(module_logger, 'check_response'):        
            # Perform validation against the Swagger schema
            try:
                jsonschema.validate(json.loads(self.response["body"]), self.response_model)
            except jsonschema.ValidationError as e:
                raise ResponseError(f'Response does not conform to the model: {e}')
        
    def get_response(self):
        with MethodLogger(module_logger, 'get_response'):
            return self.response

    def process_request(self):
        with MethodLogger(module_logger, 'process_request'):
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
        with MethodLogger(module_logger, 'process_request_implementation'):
            self.set_generic_successful_response(200, {'message': 'process_request_implementation has not been implemented.'})


