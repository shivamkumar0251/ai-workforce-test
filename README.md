# AI Workforce Test

A small, clean Python application for reusable email validation.
It includes a command-line interface, automated tests, and modern
project configuration with `pyproject.toml`.

## Project Structure

- `app/validation.py` – reusable email validation helpers
- `app/main.py` – command-line entrypoint
- `tests/test_validation.py` – automated validation tests
- `pyproject.toml` – package metadata and tooling configuration

## Setup

1. Create and activate a virtual environment.
2. Install the project with development dependencies:

```bash
python -m pip install -e ".[dev]"
```

## Usage

Run the CLI with one or more email addresses:

```bash
python -m app user@example.com bad-email@example
```

You can also use the installed console script:

```bash
email-validator user@example.com
```

## Running Tests

```bash
pytest
```

## Tech Stack

- Python
- Pytest
