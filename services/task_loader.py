def load_tasks(path: str) -> list[dict]:
    """
    Считывание данных из файла
    :param path: путь до файла
    :return: список словарей tasks
    Формат:
    [{'id': '701', 'text': '...', 'answer': '519'},...]
    """
    tasks = []

    with open(path, encoding='utf-8') as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]

    for i in range(0, len(lines), 3):
        tasks.append({
            'id': lines[i],
            'text': lines[i + 1],
            'answer': lines[i + 2],
        })
    return tasks
