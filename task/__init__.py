from utils import FileHandler, now

class Task:
    def __init__(self, description, status, created_at = now(), updated_at = now()):
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        return f'{self.description} - {self.status}'

    def create_task(self):
        file_handler = FileHandler()
        return file_handler.add_task(self)

    def delete_task(self, task_id):
        file_handler = FileHandler()
        return file_handler.delete_task(task_id)

    def update_task(self, task_id, update_data: dict):
        file_handler = FileHandler()
        return file_handler.update_task(task_id, update_data)


def get_task_by_id(id: int) -> Task:
    file_handler = FileHandler()
    tasks = file_handler._read_tasks()
    for task in tasks:
        if task.get('id') == id:
            return Task(task.get('description'), task.get('status'), task.get('created_at'), task.get('updated_at'))
    return None

def get_tasks(filter_by: str = None) -> list:
    file_handler = FileHandler()
    tasks = file_handler._read_tasks()

    if filter_by is None:
        return tasks

    response_tasks = []
    for task in tasks:
        if task.get('status') == filter_by:
            response_tasks.append(task)

    return response_tasks
