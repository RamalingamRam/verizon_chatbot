from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    ANTHROPIC_API_KEY: str
    VERIZON_COMMUNITY_URL: str
    
    class Config:
        env_file = ".env"

settings = Settings()