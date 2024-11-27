from unittest import TestCase
from unittest.mock import mock_open, patch, call

from utils import FileHandler
from task import Task


class TestFileHandler(TestCase):

    tasks = None

    @classmethod
    def setUpClass(cls):
        cls.file_handler = FileHandler()
        cls.tasks = [
            {
                'id': 1,
                'description': 'task 1',
                'status': 'todo',
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
            call('[{"id": 1, "description": "task 1", "status": "todo", "created_at": "2020-01-01", "updated_at": "2020-01-01"}]')
        ])

    def test_read_tasks(self):
        with patch('builtins.open', mock_open(read_data='[{"id": 1, "description": "task 1", "status": "todo", "created_at": "2020-01-01", "updated_at": "2020-01-01"}]')) as mocked_file:
            result = self.file_handler._read_tasks()
            mocked_file.assert_called_once_with('tasks.json', 'r')
            self.assertEqual(result, self.tasks)

    def test_delete_task(self):
        with patch('builtins.open', mock_open(read_data='[{"id": 1, "description": "task 1", "status": "todo", "created_at": "2020-01-01", "updated_at": "2020-01-01"}]')) as mocked_file:
            self.file_handler.delete_task(1)
            mocked_file.assert_any_call('tasks.json', 'w')
            mocked_file.assert_any_call('tasks.json', 'r')
            mocked_file().write.assert_has_calls([
                call('[]')
            ])

    def test_delete_one_of_many_task(self):
        data = '[{"id": 1, "description": "task 1", "status": "todo", "created_at": "2020-01-01", "updated_at": "2020-01-01"}, {"id": 2, "description": "task 2", "status": "todo", "created_at": "2024-01-01", "updated_at": "2024-01-01"}]'
        with patch('builtins.open', mock_open(read_data=data)) as mocked_file:
            self.file_handler.delete_task(1)
            mocked_file.assert_any_call('tasks.json', 'w')
            mocked_file.assert_any_call('tasks.json', 'r')
            mocked_file().write.assert_has_calls([
                call('[{"id": 2, "description": "task 2", "status": "todo", "created_at": "2024-01-01", "updated_at": "2024-01-01"}]')
            ])

    @patch('utils.now')
    def test_update_task_description(self, mock_datetime):
        data = '[{"id": 1, "description": "task 1", "status": "todo", "created_at": "2020-01-01", "updated_at": "2020-01-01"}]'
        mock_datetime.return_value = '2024-01-01'
        with patch('builtins.open', mock_open(read_data=data)) as mocked_file:
            update_dict = {'description': 'task 2'}
            self.file_handler.update_task(1, update_dict)
            mocked_file.assert_any_call('tasks.json', 'w')
            mocked_file.assert_any_call('tasks.json', 'r')
            mocked_file().write.assert_has_calls([
                call('[{"id": 1, "description": "task 2", "status": "todo", "created_at": "2020-01-01", "updated_at": "2024-01-01"}]')
            ])

    @patch('utils.now')
    def test_update_task_status(self, mock_datetime):
        data = '[{"id": 1, "description": "task 1", "status": "todo", "created_at": "2020-01-01", "updated_at": "2020-01-01"}]'
        mock_datetime.return_value = '2024-01-01'
        with patch('builtins.open', mock_open(read_data=data)) as mocked_file:
            update_dict = {'status': 'in-progress'}
            self.file_handler.update_task(1, update_dict)
            mocked_file.assert_any_call('tasks.json', 'w')
            mocked_file.assert_any_call('tasks.json', 'r')
            mocked_file().write.assert_has_calls([
                call('[{"id": 1, "description": "task 1", "status": "in-progress", "created_at": "2020-01-01", "updated_at": "2024-01-01"}]')
            ])

    def test_get_last_id(self):
        last_id = self.file_handler.get_last_id(self.tasks)
        self.assertEqual(last_id, 1)


    def test_add_task(self):
        task2 = Task('task 2', 'todo', '2024-01-01', '2024-01-01')

        with patch('builtins.open', mock_open(read_data='[{"id": 1, "description": "task 1", "status": "todo", "created_at": "2020-01-01", "updated_at": "2020-01-01"}]')) as mocked_file:
            self.file_handler.add_task(task2)
            mocked_file.assert_any_call('tasks.json', 'w')
            mocked_file.assert_any_call('tasks.json', 'r')
            mocked_file().write.assert_has_calls([
                call('[{"id": 1, "description": "task 1", "status": "todo", "created_at": "2020-01-01", "updated_at": "2020-01-01"}, {"id": 2, "description": "task 2", "status": "todo", "created_at": "2024-01-01", "updated_at": "2024-01-01"}]')
            ])
