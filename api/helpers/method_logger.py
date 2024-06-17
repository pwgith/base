"""
This module provides a context manager for logging method entry and exit.
"""

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

    def __enter__(self):
        """
        Called when entering the context.

        Returns:
            The MethodLogger instance.
        """
        self._logger.info(f"Entering {self._method_name}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Called when exiting the context.

        Args:
            exc_type: The type of the exception raised, if any.
            exc_val: The exception instance raised, if any.
            exc_tb: The traceback object associated with the exception, if any.
        """
        self._logger.info(f"Exiting {self._method_name}")
