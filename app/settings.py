from pydantic.networks import MongoDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    http_port: int = 8080
    mongodb_url: MongoDsn


settings = Settings(_env_file="../.env")
