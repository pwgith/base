from api.api_name_example.handler import handler

def test_handler():
    # Mock event and context objects
    event = {
        "key1": "value1",
        "key2": "value2"
    }

    context = {}

    # Call the handler function
    response = handler(event, context)

    # Assert that the response is as expected
    assert response["statusCode"] == 200

