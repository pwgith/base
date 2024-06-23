import pytest
from api.helpers.exceptions.lambda_base_error import LambdaBaseError

def test_lambda_base_error():
    error = LambdaBaseError("Base error")
    assert str(error) == "Message: Base error, Return Code: Undefined, Return Text: Undefined"
    assert error.getHTTPReturnCode() == "Undefined"
    assert error.getHTTPReturnText() == "Undefined"
    assert isinstance(error, LambdaBaseError)

