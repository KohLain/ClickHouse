"""ClickHouse client library - Simple wrapper around clickhouse_connect.

This package provides easy-to-use synchronous and asynchronous clients
for ClickHouse database connections.

Example usage:
    Synchronous:
    >>> from clickhouse import ClickHouseClient, ClickHouseConfig
    >>> config = ClickHouseConfig(host="localhost", database="mydb")
    >>> client = ClickHouseClient(config)
    >>> with client.get_client() as ch:
    ...     result = ch.query("SELECT * FROM mytable")

    Asynchronous:
    >>> from clickhouse import AsyncClickHouseClient, ClickHouseConfig
    >>> config = ClickHouseConfig(host="localhost", database="mydb")
    >>> client = AsyncClickHouseClient(config)
    >>> async with client.get_client() as ch:
    ...     result = await ch.query("SELECT * FROM mytable")
"""

from .client import AsyncClickHouseClient, ClickHouseClient
from .config import ClickHouseConfig
from .exceptions import ClickHouseException, ConnectionError

__version__ = "0.1.0"

__all__ = [
    "ClickHouseClient",
    "AsyncClickHouseClient",
    "ClickHouseConfig",
    "ClickHouseException",
    "ConnectionError",
]
