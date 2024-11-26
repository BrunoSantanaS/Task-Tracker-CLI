from unittest import TestCase
from unittest.mock import mock_open, patch, call

from utils import FileHandler


class TestFileHandler(TestCase):

    tasks = None

    @classmethod
    def setUpClass(cls):
        cls.file_handler = FileHandler()
        cls.tasks = [
            {
                'id': 1,
                'description': 'task 1',
                'stats': 'todo',
                'created_at': '2020-01-01',
                'updated_at': '2020-01-01'
            }
        ]

    @classmethod
    def tearDownClass(cls):
        cls.tasks = None

    @patch('builtins.open', new_callable=mock_open)
    def test_write_tasks(self, mock_open):
        self.file_handler._write_tasks(self.tasks)
        mock_open.assert_called_once_with('tasks.json', 'w')
        handle = mock_open()
        handle.write.assert_has_calls([
            call('[{"id": 1, "description": "task 1", "stats": "todo", "created_at": "2020-01-01", "updated_at": "2020-01-01"}]')
        ])

    def test_read_tasks(self):
        with patch('builtins.open', mock_open(read_data='[{"id": 1, "description": "task 1", "stats": "todo", "created_at": "2020-01-01", "updated_at": "2020-01-01"}]')) as mocked_file:
            result = self.file_handler._read_tasks()
            mocked_file.assert_called_once_with('tasks.json', 'r')
            self.assertEqual(result, self.tasks)

    # def test_delete_task(self):
    #     tasks = [{'id': 1, 'description': 'task 1', 'stats': 'todo', 'created_at': '2020-01-01', 'updated_at': '2020-01-01'}]
    #     file_handler = FileHandler()
    #     with patch('builtins.open', mock_open(read_data='[{"id": 1, "description": "task 1", "stats": "todo", "created_at": "2020-01-01", "updated_at": "2020-01-01"}]')) as mocked_file:
    #         file_handler.delete_task(1)
    #         mocked_file.assert_called_with('/tasks.json', 'w')
    #         handle = mocked_file()
    #         handle.write.assert_called_once_with('[]')
