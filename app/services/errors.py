class BaseServiceError(Exception):
    """Base class for all exceptions raised by this module."""


class BaseUserServiceError(BaseServiceError):
    """Base class for all exceptions raise by User services"""


class UserAlreadyExists(BaseUserServiceError):
    """Raised when a user already exists."""


class UserNotFound(BaseUserServiceError):
    """Raised when a user doesn't exist."""


class UserEnumValueInvalid(BaseUserServiceError):
    """Raised when a user enum value is invalid."""


class BaseProductServiceError(BaseServiceError):
    """Base class for all exceptions raise by Product services"""


class ProductNotFound(BaseProductServiceError):
    """Raised when a product doesn't exist."""
