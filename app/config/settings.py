import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    HOST: str
    PORT: int

    APP_DIR: str = os.path.abspath(os.path.dirname(os.path.dirname(__file__) or '.'))

    model_config = SettingsConfigDict(env_file=f'{APP_DIR}/config/config.env')


settings = Settings()
