import urllib.request
import re

URL = "https://gbr.mydan.online/configs"
OUTPUT_FILE = "cleaned_configs.txt"

def fetch_and_clean_keys():
    try:
        print(f"Запрос данных с {URL}...")
        # Скачиваем содержимое по ссылке
        req = urllib.request.Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')
        
        # Разбиваем на строки
        lines = content.splitlines()
        cleaned_lines = []
        
        for line in lines:
            line_str = line.strip()
            if not line_str:
                continue
            
            # Игнорируем строки, содержащие #profile-web-page-url
            if "#profile-web-page-url" in line_str:
                continue
                
            cleaned_lines.append(line_str)
        
        # Удаляем дубликаты с сохранением порядка
        final_lines = list(dict.fromkeys(cleaned_lines))
        
        # Записываем результат в файл
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write("\n".join(final_lines) + "\n")
            
        print(f"Успешно сохранено {len(final_lines)} ключей в файл {OUTPUT_FILE}")
        
    except Exception as e:
        print(f"Произошла ошибка при обновлении ключей: {e}")
        exit(1)

if __name__ == "__main__":
    fetch_and_clean_keys()
