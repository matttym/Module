import pickle


def load_table(file_path):
    """
    Загрузка таблицы из Pickle файла во внутреннее представление.

    :param file_path: Путь к Pickle файлу
    :return: Словарь с данными таблицы
    """
    try:
        with open(file_path, mode='rb') as pickle_file:
            table = pickle.load(pickle_file)

        if not isinstance(table, dict) or "headers" not in table or "rows" not in table:
            raise ValueError("Некорректное представление таблицы в файле.")

        return table
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл '{file_path}' не найден.")
    except pickle.PickleError:
        raise RuntimeError("Ошибка при чтении Pickle файла.")
    except Exception as e:
        raise RuntimeError(f"Ошибка при загрузке файла: {e}")


def save_table(table, file_path):
    """
    Сохранение таблицы из внутреннего представления в Pickle файл.

    :param table: Словарь с таблицей, содержащий ключи 'headers' и 'rows'
    :param file_path: Путь к Pickle файлу
    """
    try:
        if not isinstance(table, dict) or "headers" not in table or "rows" not in table:
            raise ValueError("Некорректное представление таблицы.")

        with open(file_path, mode='wb') as pickle_file:
            pickle.dump(table, pickle_file)
    except pickle.PickleError:
        raise RuntimeError("Ошибка при сохранении Pickle файла.")
    except Exception as e:
        raise RuntimeError(f"Ошибка при сохранении файла: {e}")
