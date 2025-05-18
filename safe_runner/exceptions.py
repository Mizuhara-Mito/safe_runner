class ResourceLimitExceeded(Exception):
    """Raised when CPU or memory limits are exceeded."""
    pass

class TimeoutExceeded(Exception):
    """Raised when execution time exceeds limit."""
    pass