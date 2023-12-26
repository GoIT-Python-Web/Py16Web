import unittest
from unittest.mock import patch, mock_open, call

from src.save_data.answer import applicant, save_applicant_data


class TestClass(unittest.TestCase):
    mock_open_file = mock_open()

    @patch('builtins.open', mock_open_file)
    def test_open_file(self):
        save_applicant_data(applicant, 'fake.csv')
        self.assertEqual(self.mock_open_file.call_count, 1, msg='Function open only one call')
        print(self.mock_open_file.call_args[0])
        print(self.mock_open_file.call_args[1])
        self.mock_open_file.assert_called()
        self.mock_open_file.assert_called_with('fake.csv', "w", encoding="utf-8")

    @patch('builtins.open', mock_open_file)
    def test_write_file(self):
        save_applicant_data(applicant, 'fake.csv')
        calls = [
            call('Ivanchuk Boryslav,101,135,150,165\n'),
            call('Kovalchuk Oleksiy,301,175,180,155\n'),
            call('Karpenko Dmitro,201,155,175,185\n'),
        ]
        self.mock_open_file().write.call_with('Ivanchuk Boryslav,101,135,150,165\n')
        self.mock_open_file().write.call_with('Karpenko Dmitro,201,155,175,185\n')
        self.mock_open_file().write.assert_has_calls(calls, any_order=True)
