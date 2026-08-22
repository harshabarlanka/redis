import redis

from app.config import settings

redis_pool = redis.ConnectionPool.from_url(
    settings.redis_url,
    decode_responses=True,   # get back str instead of bytes
    max_connections=50,
)


def get_redis() -> redis.Redis:
    """FastAPI dependency: yields a Redis client backed by the shared pool."""
    return redis.Redis(connection_pool=redis_pool)