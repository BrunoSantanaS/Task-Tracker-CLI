from datetime import datetime
import json
from os.path import exists

class FileHandler:
    def __init__(self, file_path: str = 'tasks.json'):
        self.file_path = file_path

    def _initialize_file(self):
        if not exists(self.file_path):
            with open(self.file_path, 'w') as file:
                json.dump([], file)

    def _read_tasks(self) -> list:
        self._initialize_file()
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def _write_tasks(self, tasks):
        with open(self.file_path, 'w') as file:
            file.write(json.dumps(tasks))

    def get_last_id(self, tasks: list) -> int:
        if tasks:
            return tasks[-1].get('id')
        return 0

    def add_task(self, task) -> bool:
        try:
            tasks = self._read_tasks()
            task_id = self.get_last_id(tasks) + 1
            task_data = {
                'id': task_id,
                'description': task.description,
                'status': task.status,
                'created_at': task.created_at,
                'updated_at': task.updated_at
            }
            tasks.append(task_data)
            self._write_tasks(tasks)

            return True

        except Exception as e:
            return False

    def delete_task(self, task_id) -> bool:
        try:
            tasks = self._read_tasks()
            tasks = [task for task in tasks if task.get('id') != task_id]
            self._write_tasks(tasks)
            return True

        except Exception as e:
            return False

    def update_task(self, task_id, update: dict) -> bool:
        key = list(update.keys())[0]
        value = update[key]
        try:
            tasks = self._read_tasks()
            for task in tasks:
                if task.get('id') == task_id:
                    task[key] = value
                    task['updated_at'] = now()
                    self._write_tasks(tasks)
                    return True
            return False

        except Exception as e:
            return False

def now():
    return datetime.now().isoformat()