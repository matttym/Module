def print_table(table):
    """
    Формирует текстовое представление таблицы, аналогичное выводу в консоль.

    :param table: Словарь с таблицей, содержащий ключи 'headers' и 'rows'
    :return: Строка с текстовым представлением таблицы
    """
    try:
        headers = table.get("headers", [])
        rows = table.get("rows", [])

        if not headers or not rows:
            raise ValueError("Таблица пуста или имеет некорректное представление.")

        # Формируем строки для вывода
        lines = []
        header_line = " | ".join(headers)
        lines.append(header_line)
        lines.append("-" * len(header_line))  # Разделительная линия

        for row in rows:
            lines.append(" | ".join(row))

        # Возвращаем таблицу в виде одной строки
        return "\n".join(lines)
    except Exception as e:
        raise RuntimeError(f"Ошибка при формировании текстового представления таблицы: {e}")


def save_table(table, file_path):
    """
    Сохраняет текстовое представление таблицы в файл.

    :param table: Словарь с таблицей, содержащий ключи 'headers' и 'rows'
    :param file_path: Путь к текстовому файлу
    """
    try:
        table_text = print_table(table)  # Формируем текстовое представление
        with open(file_path, mode='w', encoding='utf-8') as text_file:
            text_file.write(table_text)  # Сохраняем в файл
    except Exception as e:
        raise RuntimeError(f"Ошибка при сохранении текстового файла: {e}")
