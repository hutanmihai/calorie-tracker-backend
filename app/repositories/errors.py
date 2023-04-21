class BaseRepositoryError(Exception):
    """Base class for all exceptions raised by this module."""


class EntityNotUnique(BaseRepositoryError):
    """Raised when a unique constraint is violated."""


class EntityNotFound(BaseRepositoryError):
    """Raised when a resource is not found."""


class EnumValueInvalid(BaseRepositoryError):
    """Raised when an enum value is invalid."""
