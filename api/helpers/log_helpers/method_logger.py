"""
This module provides a context manager for logging method entry and exit.
"""
from datetime import datetime
from api.helpers.log_helpers.log_helper import prepare_log_string

class MethodLogger:
    """
    A context manager for logging method entry and exit.

    Args:
        logger: The logger object used for logging.
        method_name: The name of the method being logged.

    Example:
        logger = logging.getLogger(__name__)
        with MethodLogger(logger, 'my_method'):
            # Code to be executed
    """

    def __init__(self, logger, method_name) -> None:
        """
        Initializes a MethodLogger instance.

        Args:
            logger: The logger object used for logging.
            method_name: The name of the method being logged.
        """
        self._logger = logger
        self._method_name = method_name
        self._start_time = datetime.now()
        self._end_time = datetime.now()
        self.log_standard_info = prepare_log_string()

    def __enter__(self):
        """
        Called when entering the context.

        Returns:
            The MethodLogger instance.
        """
        self._start_time = datetime.now()
        self._logger.info(f"{self.log_standard_info}, Entering {self._method_name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Called when exiting the context.

        Args:
            exc_type: The type of the exception raised, if any.
            exc_val: The exception instance raised, if any.
            exc_tb: The traceback object associated with the exception, if any.
        """
        self._end_time = datetime.now()
        elpased_time = self._end_time - self._start_time
        exception_string = "No Exception"
        if exc_type is not None:
            exception_string = f"{exc_type.__name__}: {exc_val}"
        self._logger.info(f"{self.log_standard_info}, Exiting {self._method_name}, Elapsed time: {elpased_time}, Exception: {exception_string}")
