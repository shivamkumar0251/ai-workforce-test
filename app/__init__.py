"""Email validation application package."""

from app.validation import (
    EmailValidationError,
    is_valid_email,
    normalize_email,
    validate_email,
)

__all__ = [
    "EmailValidationError",
    "is_valid_email",
    "normalize_email",
    "validate_email",
]
