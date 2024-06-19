from helpers.log_helpers.method_logger import MethodLogger
import logging
logger = logging.getLogger(__name__)


def test_enter_exit_logging_when_info_on(caplog):
    caplog.clear()
    caplog.set_level(logging.INFO)
    with MethodLogger(logger, "test_method_execution"):
        assert "Entering test_method_execution" in caplog.text
        caplog.clear()
    assert "Exiting test_method_execution" in caplog.text
    assert "Elapsed time:" in caplog.text
    

def test_enter_exit_logging_when_info_off(caplog):
    caplog.clear()
    caplog.set_level(logging.WARNING)
    with MethodLogger(logger, "test_method_execution"):
        assert "Entering test_method_execution" not in caplog.text
        caplog.clear()
    assert "Exiting test_method_execution" not in caplog.text
    assert "Exception: No Exception" not in caplog.text

class ATestException(Exception):
    pass

def inner_function_exception():
    with MethodLogger(logger, "inner_function_exception"):
        raise ATestException("A test exception occurred")

def inner_function_no_exception():
    with MethodLogger(logger, "inner_function_no_exception"):
        pass

def test_exception(caplog):
    caplog.clear()
    caplog.set_level(logging.INFO)
    try:
        inner_function_exception()
    except ATestException:
        pass
    assert "Entering inner_function_exception" in caplog.text
    assert "Exiting inner_function_exception" in caplog.text
    assert "Exception: ATestException" in caplog.text

def test_no_exception(caplog):
    caplog.clear()
    caplog.set_level(logging.INFO)
    inner_function_no_exception()
    assert "Entering inner_function_no_exception" in caplog.text
    assert "Exiting inner_function_no_exception" in caplog.text
    assert "Exception: No Exception" in caplog.text
