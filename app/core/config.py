from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class RetailCRMConfig(BaseModel):
    version: str = "/api/v5"
    crm_url: str | None = None
    api_key: str | None = None

    @property
    def api_url(self):
        return f"{self.crm_url}{self.version}"


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    retailcrm: RetailCRMConfig = RetailCRMConfig()

    model_config = SettingsConfigDict(
        env_file=("../.env.template", "../.env"),
        env_prefix="APP_CONFIG__",
        env_nested_delimiter="__",
    )


settings = Settings()
