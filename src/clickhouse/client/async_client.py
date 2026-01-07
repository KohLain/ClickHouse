"""Asynchronous ClickHouse client wrapper."""

from contextlib import asynccontextmanager
from typing import AsyncGenerator

import clickhouse_connect
from clickhouse_connect.driver.asyncclient import AsyncClient

from ..config import ClickHouseConfig
from ..exceptions import ConnectionError


class AsyncClickHouseClient:
    """Wrapper for asynchronous ClickHouse client.

    This class provides a simple interface to create and manage
    asynchronous ClickHouse connections using the clickhouse_connect library.

    Example:
        >>> config = ClickHouseConfig(host="localhost", database="mydb")
        >>> ch_client = AsyncClickHouseClient(config)
        >>> async with ch_client.get_client() as client:
        ...     result = await client.query("SELECT * FROM mytable")
        ...     print(result.result_rows)
    """

    def __init__(self, config: ClickHouseConfig):
        """Initialize the async ClickHouse client wrapper.

        Args:
            config: ClickHouse configuration object
        """
        self.config = config

    @asynccontextmanager
    async def get_client(self) -> AsyncGenerator[AsyncClient, None]:
        """Get an async ClickHouse client as a context manager.

        This method provides an async context manager that automatically
        handles connection lifecycle. The connection is established on entry
        and closed on exit.

        Yields:
            clickhouse_connect AsyncClient instance

        Raises:
            ConnectionError: If connection fails

        Example:
            >>> async with ch_client.get_client() as client:
            ...     result = await client.query("SELECT 1")
        """
        client = None
        try:
            client = await clickhouse_connect.get_async_client(
                **self.config.to_connection_params()
            )
            yield client
        except Exception as e:
            raise ConnectionError(f"Failed to connect to ClickHouse: {e}") from e
        finally:
            if client:
                try:
                    await client.close()
                except Exception:
                    pass  # Ignore errors during cleanup