import multiprocessing as mp

from pydantic import BaseSettings


class AppSettings(BaseSettings):
    pg_database: str = "db_misis"
    pg_host: str = "localhost"
    pg_port: int = 5432
    pg_username: str = "db_misis"
    pg_password: str = "db_misis"

    uvicorn_host: str = "localhost"
    uvicorn_port: int = 8000
    uvicorn_workers: int = mp.cpu_count() * 2
    uvicorn_log_level: str = "WARNING"

    class Config:
        env_prefix = "misis_"
        env_file = ".env"


app_settings = AppSettings()
