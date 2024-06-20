from  helpers.exceptions.lambda_base_error import LambdaBaseError

class ServerError(LambdaBaseError):
    def __init__(self, message):
        super().__init__(message)
        self.return_code = 500
        self.return_text = "Internal Server Error"

class CodeAssumptionError(ServerError):
    def __init__(self, message):
        super().__init__(message)
        self.return_text = 'Code assumption broken'

class ResponseError(ServerError):
    def __init__(self, message):
        super().__init__(message)
        self.return_text = 'Response does not conform to the model'

