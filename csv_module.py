import csv


def load_table(file_path):
    """
    Загрузка таблицы из CSV файла во внутреннее представление.

    :param file_path: Путь к CSV файлу
    :return: Словарь с данными таблицы
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            data = [row for row in reader]

        if not data:
            raise ValueError("Файл пуст.")

        headers = data[0]  # Первая строка - заголовки
        rows = data[1:]  # Остальные строки - данные

        table = {
            "headers": headers,
            "rows": rows
        }
        return table
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл '{file_path}' не найден.")
    except Exception as e:
        raise RuntimeError(f"Ошибка при загрузке файла: {e}")


def save_table(table, file_path):
    """
    Сохранение таблицы из внутреннего представления в CSV файл.

    :param table: Словарь с таблицей, содержащий ключи 'headers' и 'rows'
    :param file_path: Путь к CSV файлу
    """
    try:
        headers = table.get("headers", [])
        rows = table.get("rows", [])

        if not headers or not rows:
            raise ValueError("Таблица пуста или имеет некорректное представление.")

        with open(file_path, mode='w', encoding='utf-8', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(headers)  # Записываем заголовки
            writer.writerows(rows)  # Записываем строки
    except Exception as e:
        raise RuntimeError(f"Ошибка при сохранении файла: {e}")
