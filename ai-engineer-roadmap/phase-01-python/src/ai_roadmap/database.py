import os
from collections.abc import Iterator
from functools import lru_cache

import sqlalchemy as sa
from sqlalchemy.engine import Connection, Engine

DATABASE_URL_ENV = "DATABASE_URL"


def get_database_url() -> str:
    database_url = os.getenv(DATABASE_URL_ENV)
    if database_url is None or database_url.strip() == "":
        raise RuntimeError("DATABASE_URL is not configured")
    return database_url


@lru_cache
def get_engine() -> Engine:
    database_url = get_database_url()
    return sa.create_engine(database_url)


def get_connection() -> Iterator[Connection]:
    with get_engine().begin() as connection:
        yield connection
