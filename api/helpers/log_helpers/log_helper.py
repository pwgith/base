"""
This module provides helper functions for setting and resetting standard log fields,
and preparing the log string with the current values of the standard log fields.
"""

# pylint: disable=invalid-name
_xray_trace_id = "Undefined"
_trace_id = "Undefined"
_parent_span_id = "Undefined"
_span_id = "Undefined"
_session_id = "Undefined"
_organisation_id = "Undefined"
_organisation_name = "Undefined"
_user_id = "Undefined"
_customer_id = "Undefined"
_service_name = "Undefined"
_operation_name = "Undefined"
_api_version = "Undefined"
# pylint: enable=invalid-name

def set_standard_log_fields(xray_trace_id="Undefined", trace_id="Undefined", parent_span_id="Undefined", 
                            span_id="Undefined", session_id="Undefined", organisation_id="Undefined", 
                            organisation_name="Undefined", user_id="Undefined", customer_id="Undefined",
                            service_name="Undefined", operation_name="Undefined", api_version="Undefined"):
    """
    Sets the standard log fields with the provided values.

    Args:
        xray_trace_id (str): The X-Ray trace ID.
        trace_id (str): The trace ID.
        parent_span_id (str): The parent span ID.
        span_id (str): The span ID.
        session_id (str): The session ID.
        organisation_id (str): The organisation ID.
        organisation_name (str): The organisation name.
        user_id (str): The user ID.
        customer_id (str): The customer ID.
        service_name (str): The service name.
        operation_name (str): The operation name.
        api_version (str): The API version.
    """
    reset_standard_log_fields()
    global _xray_trace_id, _trace_id, _parent_span_id, _span_id, _session_id, \
        _organisation_id, _organisation_name, _user_id, _customer_id, _service_name,\
         _operation_name, _api_version

    if xray_trace_id is not None:
        _xray_trace_id = xray_trace_id
    if trace_id is not None:
        _trace_id = trace_id
    if parent_span_id is not None:
        _parent_span_id = parent_span_id
    if span_id is not None:
        _span_id = span_id
    if session_id is not None:
        _session_id = session_id
    if organisation_id is not None:
        _organisation_id = organisation_id
    if organisation_name is not None:
        _organisation_name = organisation_name
    if user_id is not None:
        _user_id = user_id
    if customer_id is not None:
        _customer_id = customer_id
    if service_name is not None:
        _service_name = service_name
    if operation_name is not None:
        _operation_name = operation_name
    if api_version is not None:
        _api_version = api_version

def prepare_log_string():
    """
    Prepares the log string with the current values of the standard log fields.

    Returns:
        str: The log string.
    """
    log_string = f"XRayTraceId: {str(_xray_trace_id)}," + \
                 f"TraceId: {str(_trace_id)}," + \
                 f"ParentSpanId: {str(_parent_span_id)}," + \
                 f"SpanId: {str(_span_id)}," + \
                 f"SessionId: {str(_session_id)}," + \
                 f"OrganisationId: {str(_organisation_id)}," + \
                 f"OrganisationName: {str(_organisation_name)}," + \
                 f"UserId: {str(_user_id)}," + \
                 f"CustomerId: {str(_customer_id)}," + \
                 f"ServiceName: {str(_service_name)}," + \
                 f"OperationName: {str(_operation_name)}," + \
                 f"APIVersion: {str(_api_version)}"
    return log_string


def reset_standard_log_fields():
    """
    Resets all the standard log fields to their default value of "Undefined".
    Should only be used for unit testing
    """
    global _xray_trace_id, _trace_id, _parent_span_id, _span_id, _session_id, \
        _organisation_id, _organisation_name, _user_id, _customer_id, _service_name, \
        _operation_name, _api_version

    _xray_trace_id = "Undefined"
    _trace_id = "Undefined"
    _parent_span_id = "Undefined"
    _span_id = "Undefined"
    _session_id = "Undefined"
    _organisation_id = "Undefined"
    _organisation_name = "Undefined"
    _user_id = "Undefined"
    _customer_id = "Undefined"
    _service_name = "Undefined"
    _operation_name = "Undefined"
    _api_version = "Undefined"
