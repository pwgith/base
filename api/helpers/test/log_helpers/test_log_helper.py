import pytest
from helpers.log_helpers.log_helper import set_standard_log_fields, prepare_log_string, reset_standard_log_fields

def test_prepare_log_string_full():
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
    expected_log_string = "XRayTraceId: 123,TraceId: 456,ParentSpanId: 789," + \
        "SpanId: 012,SessionId: 345,OrganisationId: 678,OrganisationName: TestOrg," + \
        "UserId: 901,CustomerId: 234,ServiceName: TestService,OperationName: TestOperation," + \
        "APIVersion: 1.0"
    assert log_string == expected_log_string


def test_prepare_log_string_partial():
    # Test preparing log string with some log fields missing
    set_standard_log_fields(
        xray_trace_id="123",
        organisation_id="678",
        user_id="901",
        service_name="TestService",
        api_version="1.0"
    )
    log_string = prepare_log_string()
    expected_log_string = "XRayTraceId: 123,TraceId: Undefined,ParentSpanId: " + \
        "Undefined,SpanId: Undefined,SessionId: Undefined,OrganisationId: 678," + \
        "OrganisationName: Undefined,UserId: 901,CustomerId: Undefined," + \
        "ServiceName: TestService,OperationName: Undefined,APIVersion: 1.0"
    assert log_string == expected_log_string
