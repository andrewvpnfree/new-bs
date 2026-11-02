import os
import re
import requests


def fetch_clean_configs(url):
    """Скачивает подписку по ссылке и убирает служебные метаданные."""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        print(f"Запрос данных с {url}...")
        response = requests.get(url, headers=headers, timeout=15)

        if response.status_code != 200:
            print(f"Ошибка загрузки: статус {response.status_code}")
            return []

        # Разбиваем текст на отдельные строки
        lines = response.text.splitlines()
        clean_lines = []

        for line in lines:
            stripped = line.strip()

            # Пропускаем пустые строки и служебные строки (начинаются с #)
            if not stripped or stripped.startswith("#"):
                continue

            # Добавляем в список только чистые конфигурации
            clean_lines.append(stripped)

        return clean_lines

    except Exception as e:
        print(f"Произошла ошибка при работе с сетью: {e}")
        return []


if __name__ == "__main__":
    # Целевой URL для мобильной подписки
    TARGET_URL = "https://gbr.mydan.online/configs"

    configs = fetch_clean_configs(TARGET_URL)

    # Сохраняем результат в файл extracted_keys.txt
    with open("extracted_keys.txt", "w", encoding="utf-8") as f:
        if configs:
            f.write("\n".join(configs) + "\n")
            print(f"[+] Успешно сохранено чистых конфигураций: {len(configs)}")
        else:
            f.write("")
            print("[-] Конфигурации не найдены или произошла ошибка.")
