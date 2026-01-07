"""Configuration management for ClickHouse connections."""

from pydantic import BaseModel, Field


class ClickHouseConfig(BaseModel):
    """ClickHouse connection configuration.
    
    Attributes:
        host: ClickHouse server host
        port: ClickHouse server port
        username: Authentication username
        password: Authentication password
        database: Default database name
        secure: Use secure connection (HTTPS)
        verify: Verify SSL certificates
        connect_timeout: Connection timeout in seconds
        send_receive_timeout: Send/receive timeout in seconds
    """
    
    host: str = Field(default="localhost", description="ClickHouse server host")
    port: int = Field(default=8123, description="ClickHouse server port")
    username: str = Field(default="default", description="Authentication username")
    password: str = Field(default="", description="Authentication password")
    database: str = Field(default="default", description="Default database")
    secure: bool = Field(default=False, description="Use secure connection")
    verify: bool = Field(default=True, description="Verify SSL certificates")
    connect_timeout: int = Field(default=10, description="Connection timeout (seconds)")
    send_receive_timeout: int = Field(default=300, description="Send/receive timeout (seconds)")

    class Config:
        """Pydantic configuration."""
        frozen = False
        extra = "allow"

    def to_connection_params(self) -> dict:
        """Convert config to clickhouse_connect connection parameters.
        
        Returns:
            Dictionary of connection parameters
        """
        return {
            "host": self.host,
            "port": self.port,
            "username": self.username,
            "password": self.password,
            "database": self.database,
            "secure": self.secure,
            "verify": self.verify,
            "connect_timeout": self.connect_timeout,
            "send_receive_timeout": self.send_receive_timeout,
        }