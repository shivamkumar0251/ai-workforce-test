import pytest

from app.validation import EmailValidationError, is_valid_email, normalize_email, validate_email


@pytest.mark.parametrize(
    ("email", "expected"),
    [
        ("user@example.com", "user@example.com"),
        (" user@example.com ", "user@example.com"),
        ("First.Last@Example.COM", "First.Last@example.com"),
        ("user+tag@sub.domain.org", "user+tag@sub.domain.org"),
    ],
)
def test_validate_email_accepts_valid_addresses(email: str, expected: str) -> None:
    assert validate_email(email) == expected


@pytest.mark.parametrize(
    "email",
    [
        "",
        "missing-at.example.com",
        "user@",
        "@example.com",
        ".user@example.com",
        "user..name@example.com",
        "user@example",
        "user@-example.com",
        "user@example..com",
        "user@example.c",
        "user@example!.com",
    ],
)
def test_validate_email_rejects_invalid_addresses(email: str) -> None:
    with pytest.raises(EmailValidationError):
        validate_email(email)


def test_normalize_email_rejects_non_string_values() -> None:
    with pytest.raises(TypeError):
        normalize_email(None)  # type: ignore[arg-type]


@pytest.mark.parametrize(
    ("email", "expected"),
    [
        ("person@example.com", True),
        ("bad-email", False),
        (None, False),
    ],
)
def test_is_valid_email_returns_boolean(email: str | None, expected: bool) -> None:
    assert is_valid_email(email) is expected  # type: ignore[arg-type]
