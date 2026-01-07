"""Synchronous ClickHouse client wrapper."""

from contextlib import contextmanager
from typing import Generator

import clickhouse_connect
from clickhouse_connect.driver import Client

from ..config import ClickHouseConfig
from ..exceptions import ConnectionError


class ClickHouseClient:
    """Wrapper for synchronous ClickHouse client.

    This class provides a simple interface to create and manage
    ClickHouse connections using the clickhouse_connect library.

    Example:
        >>> config = ClickHouseConfig(host="localhost", database="mydb")
        >>> ch_client = ClickHouseClient(config)
        >>> with ch_client.get_client() as client:
        ...     result = client.query("SELECT * FROM mytable")
        ...     print(result.result_rows)
    """

    def __init__(self, config: ClickHouseConfig):
        """Initialize the ClickHouse client wrapper.

        Args:
            config: ClickHouse configuration object
        """
        self.config = config

    @contextmanager
    def get_client(self) -> Generator[Client, None, None]:
        """Get a ClickHouse client as a context manager.

        This method provides a context manager that automatically handles
        connection lifecycle. The connection is established on entry and
        closed on exit.

        Yields:
            clickhouse_connect Client instance

        Raises:
            ConnectionError: If connection fails

        Example:
            >>> with ch_client.get_client() as client:
            ...     result = client.query("SELECT 1")
        """
        client = None
        try:
            client = clickhouse_connect.get_client(**self.config.to_connection_params())
            yield client
        except Exception as e:
            raise ConnectionError(f"Failed to connect to ClickHouse: {e}") from e
        finally:
            if client:
                try:
                    client.close()
                except Exception:
                    pass  # Ignore errors during cleanup
