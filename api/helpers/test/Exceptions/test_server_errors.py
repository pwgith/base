import pytest
from helpers.exceptions.server_errors import CodeAssumptionError, ResponseError, ServerError
from helpers.exceptions.lambda_base_error import LambdaBaseError

def test_code_assumption_error():
    error = CodeAssumptionError("Code assumption error")
    assert str(error) == "Message: Code assumption error, Return Code: 500, Return Text: Code assumption broken"
    assert isinstance(error, CodeAssumptionError)
    assert isinstance(error, ServerError)
    assert isinstance(error, LambdaBaseError)

def test_response_error():
    error = ResponseError("Response error")
    assert str(error) == "Message: Response error, Return Code: 500, Return Text: Response does not conform to the model"
    assert isinstance(error, ResponseError)
    assert isinstance(error, ServerError)
    assert isinstance(error, LambdaBaseError)
