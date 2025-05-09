import unittest
import os
from app.io.input import read_from_file, read_from_file_pandas
from app.io import input


class TestInputFunctions(unittest.TestCase):
    def setUp(self):

        if not os.path.exists('data'):
            os.makedirs('data')

    # read_from_file
    def test_read_from_file_existing(self):
        # create text file
        with open('data/test_file.txt', 'w', encoding='utf-8') as file:
            file.write('Hello, world!\nThis is a test file.\n')

        result = read_from_file('data/test_file.txt')
        expected = 'Hello, world!\nThis is a test file.\n'
        self.assertEqual(result, expected)

        os.remove('data/test_file.txt')

    def test_read_from_file_non_existent(self):
        result = read_from_file('data/non_existent_file.txt')
        self.assertEqual(result, 'File not found.')

    def test_read_from_file_empty(self):
        # empty file
        with open('data/empty_file.txt', 'w', encoding='utf-8') as file:
            file.write('')

        result = read_from_file('data/empty_file.txt')
        self.assertEqual(result, '')

        os.remove('data/empty_file.txt')

    def test_read_from_file_pandas_existing(self):
        # Викликаємо функцію для зчитування з файлу
        result = input.read_from_file_pandas('data/test_file_pandas.txt')

        # Перевіряємо, чи містить результат очікувані дані
        self.assertIn('Hello this is a test file.', result)
        self.assertIn('It contains multiple lines of text.', result)

    def test_read_from_file_pandas_nonexistent(self):
        # Перевіряємо, що буде, якщо файл не існує
        result = input.read_from_file_pandas('data/nonexistent_file.txt')

        # Перевіряємо, чи повертається правильне повідомлення про помилку
        self.assertEqual(result, "File not found.")

    def test_read_from_file_pandas_valid_format(self):
        # Створюємо правильний файл для pandas
        with open('data/test_file_pandas_valid.txt', 'w', encoding='utf-8') as file:
            file.write("Hello, this is a test file.\nIt contains multiple lines of text.\n")

        # Перевіряємо результат
        result = input.read_from_file_pandas('data/test_file_pandas_valid.txt')

        # Перевіряємо, чи результат є правильним (повинно бути зчитано зміст файлу)
        expected = "Hello, this is a test file.\nIt contains multiple lines of text."
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
