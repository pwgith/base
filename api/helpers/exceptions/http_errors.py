from api.helpers.exceptions.lambda_base_error import LambdaBaseError

class HTTPError(LambdaBaseError):
    pass

class BadRequestError(HTTPError):
    def __init__(self, message):
        super().__init__(message)
        self.return_code = 400
        self.return_text = 'Bad Request'
