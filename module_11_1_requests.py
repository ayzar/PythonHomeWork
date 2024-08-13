import requests
from bs4 import BeautifulSoup
import csv
import json

# Функция для выполнения GET-запроса с обработкой ошибок
def get_page_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на HTTP ошибки
        return response.text
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP ошибка: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Ошибка соединения: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Превышено время ожидания: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Неизвестная ошибка: {req_err}")
    return None

# Функция для работы с сессией (сохранение состояния, например, cookies)
def fetch_with_session(urls):
    session = requests.Session()
    results = []
    for url in urls:
        try:
            response = session.get(url)
            response.raise_for_status()
            results.append(response.text)
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе {url}: {e}")
    return results

# Парсинг содержимого страницы
def parse_page(content):
    soup = BeautifulSoup(content, 'html.parser')

    # Извлечение всех заголовков <h2>
    h2_tags = soup.find_all('h2')
    headers = [h2.text.strip() for h2 in h2_tags]
    # Выводим текст каждого заголовка
    for idx, h2 in enumerate(h2_tags, start=1):
            print(f"Заголовок {idx}: {h2.text}")


    # Извлечение всех ссылок на странице
    links = soup.find_all('a')
    link_data = [{"text": link.text.strip(), "href": link.get('href')} for link in links]


    # Извлечение всех изображений на странице
    images = soup.find_all('img')
    image_data = [{"alt": img.get('alt'), "src": img.get('src')} for img in images]

    return {"headers": headers, "links": link_data, "images": image_data}

# Запись данных в CSV файл
def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Заголовок", "Ссылка", "Изображение"])
        max_len = max(len(data["headers"]), len(data["links"]), len(data["images"]))
        for i in range(max_len):
            row = [
                data["headers"][i] if i < len(data["headers"]) else "",
                data["links"][i]["href"] if i < len(data["links"]) else "",
                data["images"][i]["src"] if i < len(data["images"]) else ""
            ]
            writer.writerow(row)

# Запись данных в JSON файл
def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# Основная программа
def main():
    url = 'https://runes-magic.ru/runicheskaya-magiya/magiya-skandinavskih-run'

    # Используем сессию для получения нескольких страниц
    urls = [url, 'https://runes-magic.ru/']
    pages_content = fetch_with_session(urls)

    for i, content in enumerate(pages_content, start=1):
        if content:
            data = parse_page(content)

            # Сохраняем результаты парсинга в CSV
            csv_filename = f'parsed_data_{i}.csv'
            save_to_csv(data, csv_filename)
            print(f"Данные сохранены в CSV файл: {csv_filename}")

            # Сохраняем результаты парсинга в JSON
            json_filename = f'parsed_data_{i}.json'
            save_to_json(data, json_filename)
            print(f"Данные сохранены в JSON файл: {json_filename}")

if __name__ == "__main__":
    main()
