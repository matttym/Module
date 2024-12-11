import csv_module
import pickle_module
import text_module


def main():
    # Пример данных
    table = {
        "headers": ["Name", "Age", "City"],
        "rows": [
            ["Alice", "30", "New York"],
            ["Bob", "25", "Los Angeles"],
            ["Charlie", "35", "Chicago"]
        ]
    }

    # Пути к файлам
    csv_file = "table.csv"
    pickle_file = "table.pkl"
    text_file = "table.txt"

    # Сохранение таблицы в различных форматах
    csv_module.save_table(table, csv_file)
    pickle_module.save_table(table, pickle_file)
    text_module.save_table(table, text_file)
    print(f"Таблица сохранена в файлы: {csv_file}, {pickle_file}, {text_file}")

    # Загрузка таблицы из CSV
    loaded_csv_table = csv_module.load_table(csv_file)
    print(f"\nЗагруженная таблица из CSV:\n{text_module.print_table(loaded_csv_table)}")

    # Загрузка таблицы из Pickle
    loaded_pickle_table = pickle_module.load_table(pickle_file)
    print(f"\nЗагруженная таблица из Pickle:\n{text_module.print_table(loaded_pickle_table)}")


if __name__ == "__main__":
    main()
