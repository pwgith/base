from helpers.method_logger import MethodLogger
import logging
logger = logging.getLogger(__name__)


def test_enter_exit_logging_when_info_on(caplog):
    caplog.clear()
    caplog.set_level(logging.INFO)
    with MethodLogger(logger, "test_method_execution"):
        assert "Entering test_method_execution" in caplog.text
        caplog.clear()
    assert "Exiting test_method_execution" in caplog.text
    

def test_enter_exit_logging_when_info_off(caplog):
    caplog.clear()
    caplog.set_level(logging.WARNING)
    with MethodLogger(logger, "test_method_execution"):
        assert "Entering test_method_execution" not in caplog.text
        caplog.clear()
    assert "Exiting test_method_execution" not in caplog.text


if __name__ == '__main__':
    unittest.main()