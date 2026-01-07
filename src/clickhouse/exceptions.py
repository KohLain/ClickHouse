"""Custom exceptions for ClickHouse client operations."""


class ClickHouseException(Exception):
    """Base exception for ClickHouse operations."""
    pass


class ConnectionError(ClickHouseException):
    """Raised when connection to ClickHouse fails."""
    pass