from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql+psycopg://postgres:postgres@localhost:5433/catalog"

    cache_ttl_seconds: int = 60

    class config:
        env_file = ".env"

settings = Settings()