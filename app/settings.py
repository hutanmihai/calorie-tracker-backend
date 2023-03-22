from pydantic import BaseSettings, Field, PostgresDsn, validator


class AppSettings(BaseSettings):
    app_host: str = Field(..., env="APP_HOST")
    app_port: str = Field(..., env="APP_PORT")

    database_hostname: str = Field(..., env="DATABASE_HOSTNAME")
    database_user: str = Field(..., env="DATABASE_USER")
    database_password: str = Field(..., env="DATABASE_PASSWORD")
    database_port: str = Field(..., env="DATABASE_PORT")
    database_db: str = Field(..., env="DATABASE_DB")
    sqlalchemy_database_url: str = ""

    @validator("sqlalchemy_database_url")
    def _assemble_db_connection(cls, v: str, values: dict[str, str]) -> str:
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            user=values["database_user"],
            password=values["database_password"],
            host=values["database_hostname"],
            port=values["database_port"],
            path=f"/{values['database_db']}",
        )


settings: AppSettings = AppSettings()
