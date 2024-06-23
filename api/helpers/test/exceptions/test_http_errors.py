import pytest
from api.helpers.exceptions.http_errors import HTTPError, BadRequestError
from api.helpers.exceptions.lambda_base_error import LambdaBaseError

def test_bade_request_error():
    error = BadRequestError("Bad request error")
    assert str(error) == "Message: Bad request error, Return Code: 400, Return Text: Bad Request"
    assert isinstance(error, BadRequestError)
    assert isinstance(error, HTTPError)
    assert isinstance(error, LambdaBaseError)

