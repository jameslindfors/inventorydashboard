from typing import Set
from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "INVENTORY_SERVICE"
    APP_VERSION: str = "0.0.1"
    URI_PREFIX: str = "inventory/api"
    POSTGRESQL_USERNAME: str = "postgres"
    POSTGRESQL_PASSWORD: str = "password"
    POSTGRESQL_DATABASE: str = "dev"


settings = Settings()