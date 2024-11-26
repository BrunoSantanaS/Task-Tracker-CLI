from utils import FileHandler

class Task:
    def __init__(self, description, status, created_at, updated_at):
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        return f'{self.description} - {self.status}'

    def create_task(self):
        # Receive the task object and save it to a file
        return None