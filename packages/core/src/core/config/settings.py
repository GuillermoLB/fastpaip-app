"""
Defines the centralized configuration for the entire application.

This module uses Pydantic's BaseSettings to load configuration from environment
variables and .env files. It conditionally loads a '.env.test' file if the
'TESTING' environment variable is set.
"""
import os
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

# --- Determine which .env file to load ---
env_file = ".env.test" if os.getenv("TESTING") else ".env"
print(f"LOADING SETTINGS FROM: {env_file}")


class OpenAISettings(BaseModel):
    """Configuration for the external OpenAI API."""
    api_key: str

# --- The main, top-level Settings class ---

class Settings(BaseSettings):
    """
    The main settings object, composed of nested configuration models.
    """
    model_config = SettingsConfigDict(
        env_file=env_file,
        env_nested_delimiter='__',
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    log_level: str = "DEBUG"
    pythonpath: str = "."

    # The attribute names here (aws, postgres) are the prefixes for the env vars
    openai_api: OpenAISettings

# --- Create a single, importable instance of the settings ---
settings = Settings()