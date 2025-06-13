from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    base_url: str = Field(..., validation_alias='BASE_URL')
    username: str = Field(..., validation_alias='USERNAME')
    password: str = Field(..., validation_alias='PASSWORD')

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8"
    }


settings = Settings() 