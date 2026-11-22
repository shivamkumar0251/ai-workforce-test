from __future__ import annotations

import argparse

from app.validation import EmailValidationError, validate_email


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate one or more email addresses.")
    parser.add_argument("emails", nargs="+", help="Email addresses to validate")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    has_errors = False
    for email in args.emails:
        try:
            normalized = validate_email(email)
            print(f"VALID   {normalized}")
        except EmailValidationError as error:
            print(f"INVALID {email}: {error}")
            has_errors = True

    return 1 if has_errors else 0
