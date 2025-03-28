import pandas as pd

def read_from_console():
    """
    Reads user input from the console.

    :return: The string entered by the user.
    """
    return input("Enter text: ")

def read_from_file(filepath):
    """
    Reads the contents of a text file from the specified path.

    :param filepath: The path to the file.
    :return: The contents of the file as a string.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."


def read_from_file_pandas(filepath):
    """
    Reads the content of a text file using pandas.

    :param filepath: Path to the file.
    :return: File content as a string.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.readlines()

        return '\n'.join(line.strip() for line in content)

    except FileNotFoundError:
        return "File not found."
    except pd.errors.ParserError as e:
        return f"Error reading file: {e}"
    except Exception as e:
        return f"Error reading file: {e}"