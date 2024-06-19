import jsonschema
import api.helpers.exceptions.lambda_base_error as lambda_base_error
import logging

class LambdaHandler:
    def __init__(self, request_model, response_model):
        self.event = None
        self.context = None
        self.headers = None
        self.message = None
        self.response = None
        if request_model is None:
            raise lambda_base_error.CodeAssumptionError('request_model is not defined')
        self.request_model = request_model
        if response_model is None:
            raise lambda_base_error.CodeAssumptionError('response_model model is not defined')
        self.response_model = response_model
        

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

    def set_successful_response(self, status_code, body):
        self.response = {
            'statusCode': status_code,
            'body': json.dumps(body),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }

    def build_error_response(self, status_code, error_message):
        return {
            'statusCode': status_code,
            'body': json.dumps({'error': error_message}),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            }
        }
    
    def check_request(self):
        if self.event is None:
            raise lambda_base_error.CodeAssumptionError('Event is not defined')
        # Perform validation against the Swagger schema
        # You can use a library like jsonschema to validate the message against the model
        # Here's an example using jsonschema:
        try:
            jsonschema.validate(self.request_model, self.event)
        except jsonschema.ValidationError as e:
            raise lambda_base_error.BadRequestError(f'Request does not conform to the model: {e}')

    def check_response(self):
        if self.event is None:
            raise lambda_base_error.CodeAssumptionError('Event is not defined')
        # Perform validation against the Swagger schema
        # You can use a library like jsonschema to validate the message against the model
        # Here's an example using jsonschema:
        try:
            jsonschema.validate(self.response_model, self.response)
        except jsonschema.ValidationError as e:
            raise lambda_base_error.ResponseError(f'Response does not conform to the model: {e}')

    def process_request(self, event, context):
        result = False
        try:
            self.event = event
            self.context = context
            self.message = json.loads(self.get_body())
            self.headers = self.event.get('headers')
            self.check_request()
            result = self.process_request_implementation
            self.check_response()
        except lambda_base_error.LambdaError as e:
            result = False
            self.get_logger().error(f'Lambda error: {e}')
            self.response = self.build_error_response(e.getHTTPReturnCode(), e.getHTTPReturnText())
        return(result)
        
    def process_request_implementation(self):
        # Must call the set_succesul_response method on success
        # and raise a LambdaError on failure
        pass
