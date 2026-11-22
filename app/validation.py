from __future__ import annotations

import re

LOCAL_PART_PATTERN = re.compile(r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+$")
DOMAIN_LABEL_PATTERN = re.compile(r"^[A-Za-z0-9-]+$")


class EmailValidationError(ValueError):
    """Raised when an email address fails validation."""


def normalize_email(email: str) -> str:
    if not isinstance(email, str):
        raise TypeError("email must be a string")

    normalized = email.strip()
    if not normalized:
        raise EmailValidationError("email must not be empty")

    return normalized


def validate_email(email: str) -> str:
    normalized = normalize_email(email)

    if len(normalized) > 254:
        raise EmailValidationError("email must be 254 characters or fewer")

    if normalized.count("@") != 1:
        raise EmailValidationError("email must contain a single @ symbol")

    local_part, domain = normalized.split("@", maxsplit=1)
    if not local_part:
        raise EmailValidationError("email must include a local part")
    if not domain:
        raise EmailValidationError("email must include a domain")
    if len(local_part) > 64:
        raise EmailValidationError("local part must be 64 characters or fewer")
    if local_part.startswith(".") or local_part.endswith("."):
        raise EmailValidationError("local part must not start or end with a dot")
    if ".." in local_part:
        raise EmailValidationError("local part must not contain consecutive dots")
    if not LOCAL_PART_PATTERN.fullmatch(local_part):
        raise EmailValidationError("local part contains unsupported characters")

    normalized_domain = domain.lower()
    if ".." in normalized_domain:
        raise EmailValidationError("domain must not contain consecutive dots")

    labels = normalized_domain.split(".")
    if len(labels) < 2:
        raise EmailValidationError("domain must contain a dot")

    for label in labels:
        if not label:
            raise EmailValidationError("domain labels must not be empty")
        if len(label) > 63:
            raise EmailValidationError("domain labels must be 63 characters or fewer")
        if label.startswith("-") or label.endswith("-"):
            raise EmailValidationError("domain labels must not start or end with a hyphen")
        if not DOMAIN_LABEL_PATTERN.fullmatch(label):
            raise EmailValidationError("domain contains unsupported characters")

    if len(labels[-1]) < 2 or not any(char.isalpha() for char in labels[-1]):
        raise EmailValidationError("top-level domain must contain at least two letters")

    return f"{local_part}@{normalized_domain}"


def is_valid_email(email: str) -> bool:
    try:
        validate_email(email)
    except (TypeError, EmailValidationError):
        return False

    return True
