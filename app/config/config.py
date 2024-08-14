import os

from pydantic_settings import BaseSettings, SettingsConfigDict

APP_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__) or '.'))


class Config(BaseSettings):
    host: str = NotImplemented
    port: int = NotImplemented

    model_config = SettingsConfigDict(env_file=f'{APP_DIR}/config/config.env')


config = Config()
