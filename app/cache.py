import json
import logging

import redis

from app.config import settings
from app.schemas import ProductOut

logger = logging.getLogger("cache")


def _key(product_id: int) -> str:
    return f"product:{product_id}"


def get_cached_product(r: redis.Redis, product_id: int) -> dict | None:
    try:
        raw = r.get(_key(product_id))
        return json.loads(raw) if raw else None
    except redis.RedisError:
        logger.warning("Redis unavailable on read, falling back to DB", exc_info=True)
        return None


def set_cached_product(r: redis.Redis, product: ProductOut) -> None:
    try:
        r.set(_key(product.id), product.model_dump_json(), ex=settings.cache_ttl_seconds)
    except redis.RedisError:
        logger.warning("Redis unavailable on write, skipping cache write", exc_info=True)


def invalidate_product(r: redis.Redis, product_id: int) -> None:
    try:
        r.delete(_key(product_id))
    except redis.RedisError:
        logger.warning("Redis unavailable on invalidate", exc_info=True)