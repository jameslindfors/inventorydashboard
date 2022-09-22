"""Config Module"""
from pydantic import BaseSettings

class Settings(BaseSettings):
    """
        Settings Data Class
    """
    app_name: str = "INVENTORY_SERVICE"
    app_version: str = "0.0.1"
    uri_prefix: str = "inventory/api"
    postgresql_username: str = "postgres"
    postgresql_password: str = "password"
    postgresql_database: str = "dev"


settings = Settings()
