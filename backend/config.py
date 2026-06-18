import os
from pathlib import Path

import toml


PROJECT_ROOT = Path(__file__).resolve().parent.parent
SECRETS_FILE = PROJECT_ROOT / ".streamlit" / "secrets.toml"


def read_secret(key: str, default: str = "") -> str:
    if key in os.environ:
        return os.environ[key]

    if not SECRETS_FILE.exists():
        return default

    secrets = toml.load(SECRETS_FILE)

    if key in secrets:
        return secrets[key]

    return default


def get_database_url() -> str:
    database_url = read_secret("DATABASE_URL")

    if not database_url:
        raise RuntimeError(
            "DATABASE_URL is missing. Add it to .streamlit/secrets.toml."
        )

    if database_url.startswith("postgresql://"):
        database_url = database_url.replace(
            "postgresql://",
            "postgresql+psycopg://",
            1,
        )

    return database_url


def get_api_base_url() -> str:
    return read_secret("API_BASE_URL", "http://127.0.0.1:8000")


def get_gemini_api_key() -> str:
    api_key = read_secret("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is missing. Add it to .streamlit/secrets.toml."
        )

    return api_key
