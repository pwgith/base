import pytest
from api.helpers.log_helper import set_standard_log_fields, prepare_log_string

def test_set_standard_log_fields():
    # Test setting all log fields
    set_standard_log_fields(
        xray_trace_id="123",
        trace_id="456",
        parent_span_id="789",
        span_id="012",
        session_id="345",
        organisation_id="678",
        organisation_name="TestOrg",
        user_id="901",
        customer_id="234",
        service_name="TestService",
        operation_name="TestOperation",
        api_version="1.0"
    )
    assert _xray_trace_id == "123"
    assert _trace_id == "456"
    assert _parent_span_id == "789"
    assert _span_id == "012"
    assert _session_id == "345"
    assert _organisation_id == "678"
    assert _organisation_name == "TestOrg"
    assert _user_id == "901"
    assert _customer_id == "234"
    assert _service_name == "TestService"
    assert _operation_name == "TestOperation"
    assert _api_version == "1.0"

    # Test setting only some log fields
    set_standard_log_fields(
        xray_trace_id="123",
        organisation_id="678",
        user_id="901",
        service_name="TestService",
        api_version="1.0"
    )
    assert _xray_trace_id == "123"
    assert _trace_id == "Undefined"
    assert _parent_span_id == "Undefined"
    assert _span_id == "Undefined"
    assert _session_id == "Undefined"
    assert _organisation_id == "678"
    assert _organisation_name == "Undefined"
    assert _user_id == "901"
    assert _customer_id == "Undefined"
    assert _service_name == "TestService"
    assert _operation_name == "Undefined"
    assert _api_version == "1.0"

def test_prepare_log_string():
    # Test preparing log string with all log fields set
    set_standard_log_fields(
        xray_trace_id="123",
        trace_id="456",
        parent_span_id="789",
        span_id="012",
        session_id="345",
        organisation_id="678",
        organisation_name="TestOrg",
        user_id="901",
        customer_id="234",
        service_name="TestService",
        operation_name="TestOperation",
        api_version="1.0"
    )
    log_string = prepare_log_string()
    expected_log_string = "X-Ray Trace ID: 123, Trace ID: 456, Parent Span ID: 789, Span ID: 012, Session ID: 345, Organisation ID: 678, Organisation Name: TestOrg, User ID: 901, Customer ID: 234, Service Name: TestService, Operation Name: TestOperation, API Version: 1.0"
    assert log_string == expected_log_string

    # Test preparing log string with some log fields missing
    set_standard_log_fields(
        xray_trace_id="123",
        organisation_id="678",
        user_id="901",
        service_name="TestService",
        api_version="1.0"
    )
    log_string = prepare_log_string()
    expected_log_string = "X-Ray Trace ID: 123, Trace ID: Undefined, Parent Span ID: Undefined, Span ID: Undefined, Session ID: Undefined, Organisation ID: 678, Organisation Name: Undefined, User ID: 901, Customer ID: Undefined, Service Name: TestService, Operation Name: Undefined, API Version: 1.0"
    assert log_string == expected_log_string