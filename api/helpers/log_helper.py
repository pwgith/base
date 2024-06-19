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

def set_standard_log_fields(xray_trace_id = None,
                            trace_id = None,
                            parent_span_id = None,
                            span_id = None,
                            session_id = None,
                            organisation_id = None,
                            organisation_name = None,
                            user_id = None,
                            customer_id = None,
                            service_name = None,
                            operation_name = None,
                            api_version = None):
    if _xray_trace_id is not None:
        _xray_trace_id = xray_trace_id
    if _trace_id is not None:
        _trace_id = trace_id
    if _parent_span_id is not None:
        _parent_span_id = parent_span_id
    if _span_id is not None:
        _span_id = span_id
    if _session_id is not None:
        _session_id = session_id
    if _organisation_id is not None:
        _organisation_id = organisation_id
    if _organisation_name is not None:
        _organisation_name = organisation_name
    if _user_id is not None:
        _user_id = user_id
    if _customer_id is not None:
        _customer_id = customer_id
    if _service_name is not None:
        _service_name = service_name
    if _operation_name is not None:
        _operation_name = operation_name
    if _api_version is not None:
        _api_version = api_version

def prepare_log_string():
    log_string =    f"XrayTraceId: {_xray_trace_id}," + \
                    f"TraceId: {_trace_id}," + \
                    f"ParentSpanId: {_parent_span_id}," + \
                    f"SpanId: {_span_id}," + \
                    f"SessionId: {_session_id}," + \
                    f"OrganisationId: {_organisation_id}," + \
                    f"OrganisationName: {_organisation_name}," + \
                    f"UserId: {_user_id}," + \
                    f"CustomerId: {_customer_id}," + \
                    f"ServiceName: {_service_name}," + \
                    f"OperationName: {_operation_name}," + \
                    f"ApiVersion: {_api_version}"
    return log_string
