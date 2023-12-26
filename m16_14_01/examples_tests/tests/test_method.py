import unittest
from unittest.mock import patch, mock_open

from src.method.main import read_contacts_from_file, write_contacts_to_file


class TestClass(unittest.TestCase):
    mock_open_file = mock_open()
    contacts = [{'name': 'Oleksii', 'age': 18}, {'name': 'Dmitriy', 'age': 29}, {'name': 'Сергій', 'age': 28},
                {'name': 'Igor', 'age': 90}]

    @patch('json.dump')
    @patch('builtins.open', mock_open_file)
    def test_write_one(self, mock_json_dump):
        write_contacts_to_file('fake.json', self.contacts)
        self.mock_open_file.assert_called_with('fake.json', "w")
        mock_json_dump.assert_called()
        mock_json_dump.assert_called_with({"contacts": self.contacts}, self.mock_open_file())

    @patch('json.load')
    @patch('builtins.open', mock_open_file)
    def test_write(self, load_mock):
        load_mock.return_value = {"contacts": self.contacts}
        result = read_contacts_from_file('fake.json')
        self.mock_open_file.assert_called_with('fake.json', "r")
        load_mock.assert_called()
        load_mock.assert_called_with(self.mock_open_file())
        self.assertListEqual(result, self.contacts)

