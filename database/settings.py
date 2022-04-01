from pydantic import BaseSettings


class Settings(BaseSettings):
  database_url: str
  database_url_sync: str

  class Config:
    env_file = '.env'


settings = Settings()