from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

# -------------------CONFIGURE OUR ENVIROMENT VARIABLES USING PYDANTIC-------------------

class AppSettings(BaseSettings):
    database_hostname:str
    database_username:str
    database_name:str
    database_port:str
    database_password:str
    secret_key:str
    algorithm:str
    access_token_expire_minutes:int

    class Config:
        env_file=".env"

settings = AppSettings()