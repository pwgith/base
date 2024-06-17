
class MethodLogger:
    def __init__(self, logger, method_name) -> None:
        self._logger = logger
        self._method_name = method_name

    def __enter__(self):
        self._logger.info(f"Entering {self._method_name}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._logger.info(f"Exiting {self._method_name}")
        
