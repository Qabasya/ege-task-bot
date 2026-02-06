from services.dbloader import load_tasks_to_db

FILE_NAME = "tasks/task_8.txt"
DB_NAME = "db/ege_bot_db.db"
TABLE = "task_8"

load_tasks_to_db(FILE_NAME, DB_NAME, TABLE)
