# == Загрузка заданий из текстовых файлов в базу данных ==#
import sqlite3


def load_tasks_to_db(file_path: str, db_path: str, table_name: str) -> None:
    """
    Функция для чтения заданий из файла и загрузки из в базу данных.
    Используется для создания новой таблицы!
    Для добавления заданий в существующую будет другая функция.
    :param file_path: путь до файла
    :param db_path: путь до базы данных
    :param table_name: название таблицы
    :return:
    """
    # Подключение к базе
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    # Создание новой таблицы
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_number INTEGER NOT NULL,
        task_text TEXT NOT NULL,
        correct_answer INTEGER NOT NULL
            )
        ''')

    # Чтение файла
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]

        tasks_to_insert = []  # список с кортежами-заданиями
        for i in range(0, len(lines), 3):
            task_data = lines[i:i + 3]
            if len(task_data) == 3:
                tasks_to_insert.append(tuple(task_data))

    # Вставка всех данных
    cursor.executemany(
        f'''INSERT INTO {table_name} (task_number, task_text, correct_answer) 
                VALUES (?, ?, ?)''',
        tasks_to_insert
    )

    connection.commit()
    connection.close()

    #logging
    print(f'''Задания в количестве {len(tasks_to_insert)} штук успешно загружены в таблицу {table_name}''')

