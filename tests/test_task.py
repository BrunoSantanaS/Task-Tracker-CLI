from datetime import datetime
from unittest import TestCase

from task import Task


# class TestTask(TestCase):
#     def test_create_task(self):
#         created_at = datetime.now().isoformat()
#         updated_at = datetime.now().isoformat()

#         task = Task('description', 'status', created_at, updated_at)
#         creation_response = task.create_task()

#         self.assertIsNotNone(creation_response)