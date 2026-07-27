from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str

    DEBUG: bool

    DATABASE_URL: str

    SECRET_KEY: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int

    MAINTENANCE_INTERVAL_DAYS: int

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()