#!/usr/bin/env python3
# test_environment.py

print("=" * 50)
print("Проверка окружения проекта Яндекс Афиша")
print("=" * 50)

# 1. Проверка импортов
print("\n1. Проверка импортов:")
try:
    import pandas as pd
    print("✓ pandas")
except ImportError:
    print("✗ pandas")

try:
    import numpy as np
    print("✓ numpy")
except ImportError:
    print("✗ numpy")

try:
    import matplotlib.pyplot as plt
    print("✓ matplotlib")
except ImportError:
    print("✗ matplotlib")

try:
    from sqlalchemy import create_engine
    print("✓ sqlalchemy")
except ImportError:
    print("✗ sqlalchemy")

try:
    from phik import phik_matrix
    print("✓ phik")
except ImportError:
    print("✗ phik")

# 2. Проверка файлов проекта
print("\n2. Проверка файлов проекта:")
import os

files_to_check = [
    'analysis.ipynb',
    'requirements.txt',
    'README.md',
    '.gitignore',
    '.env.example',
    'config/database_config.py',
    '.env'
]

for file in files_to_check:
    if os.path.exists(file):
        size = os.path.getsize(file)
        print(f"✓ {file} ({size} bytes)")
    else:
        print(f"✗ {file} (не найден)")

# 3. Проверка конфигурации БД
print("\n3. Проверка конфигурации БД:")
try:
    import sys
    sys.path.append('config')
    from database_config import DatabaseConfig
    
    # Пытаемся загрузить конфигурацию
    config = DatabaseConfig.get_config_dict()
    print("✓ Конфигурация БД загружена")
    
    # Проверяем наличие обязательных полей
    required_fields = ['user', 'host', 'port', 'db']
    for field in required_fields:
        if field in config and config[field]:
            print(f"  ✓ {field}: {config[field]}")
        else:
            print(f"  ✗ {field}: отсутствует")
            
except Exception as e:
    print(f"✗ Ошибка при загрузке конфигурации: {e}")

print("\n" + "=" * 50)
print("Проверка завершена!")
print("=" * 50)

# 4. Рекомендации
print("\nРекомендации:")
print("1. Установите недостающие зависимости: pip install -r requirements.txt")
print("2. Запустите ноутбук: jupyter notebook analysis.ipynb")
print("3. Проверьте подключение к БД в первой ячейке ноутбука")
