# config/database_config.py
import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

class DatabaseConfig:
    """Конфигурация подключения к базе данных"""

    @staticmethod
    def get_connection_string():
        """Возвращает строку подключения к БД"""
        return f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

    @staticmethod
    def get_config_dict():
        """Возвращает конфигурацию в виде словаря"""
        return {
            'user': os.getenv('DB_USER'),
            'pwd': os.getenv('DB_PASSWORD'),
            'host': os.getenv('DB_HOST'),
            'port': os.getenv('DB_PORT'),
            'db': os.getenv('DB_NAME')
        }
