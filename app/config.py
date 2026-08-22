from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # --- Postgres ---
    database_url: str = "postgresql+psycopg://postgres:postgres@localhost:5432/catalog"

    # --- Redis ---
    redis_url: str = "redis://localhost:6379/0"

    # --- Cache ---
    cache_ttl_seconds: int = 60          # how long a cached product stays fresh

    class Config:
        env_file = ".env"


settings = Settings()