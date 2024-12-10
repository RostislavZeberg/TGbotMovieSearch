import os

from dotenv import load_dotenv
from pydantic import SecretStr, StrictStr
from pydantic_settings import BaseSettings

load_dotenv()


class SiteSettings(BaseSettings):
    """
    Класс обеспечивает скрытую передачу чувствительных данных
    """
    bot_token: SecretStr = os.getenv('BOT_TOKEN', None)
    api_key: SecretStr = os.getenv('SITE_API', None)
    host_api: StrictStr = os.getenv('HOST_API', None)


site = SiteSettings()

DEFAULT_COMMANDS = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку")
)
