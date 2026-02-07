# == Работа с базой данных ==#
import sqlite3


def load_tasks_to_db(file_path: str, db_path: str, table_name: str) -> None:
    """
    Функция для чтения заданий из файла и загрузки из в базу данных.
    Используется для создания новой таблицы!
    Для добавления заданий в существующую будет другая функция.
    Эту используйте только 1 раз
    :param file_path: путь до файла
    :param db_path: путь до базы данных
    :param table_name: название таблицы
    :return:
    """
    # Подключение к базе
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

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
            lines = [line.strip() for line in file if line.strip()]

        tasks_to_insert = []

        for i in range(0, len(lines), 3):
            task_number = int(lines[i])
            task_text = lines[i + 1]
            correct_answer = int(lines[i + 2])

            tasks_to_insert.append(
                (task_number, task_text, correct_answer)
            )

        # Вставка всех данных
        cursor.executemany(
            f'''INSERT INTO {table_name}
                (task_number, task_text, correct_answer)
                VALUES (?, ?, ?)''',
            tasks_to_insert
        )

    # logging
    print(f'''Задания в количестве {len(tasks_to_insert)} штук успешно загружены в таблицу {table_name}''')


def load_tasks_from_db(db_path: str, table_name: str) -> list[dict]:
    """
    Функция для загрузки заданий из базы данных.
    Нет проверки корректности имени таблиц!
    :param db_path: путь до базы данных
    :param table_name: название таблицы (task_7, task_8 и тд)
    :return: список заданий
    """
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        cursor.execute(f"""
            SELECT task_number, task_text, correct_answer
            FROM {table_name}
            ORDER BY task_number
        """)
        rows = cursor.fetchall()
        tasks = [
            {
                'id': row[0],
                'text': row[1],
                'answer': row[2]
            }
            for row in rows
        ]
        return tasks
