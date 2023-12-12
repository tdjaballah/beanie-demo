from pydantic.networks import MongoDsn
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    mongodb_url: MongoDsn


settings = Settings(_env_file="../.env")
