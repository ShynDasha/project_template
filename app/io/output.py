def write_to_console(text):
    """
    Prints the given text to the console.

    :param text: The text to be printed.
    """
    print(text)

def write_to_file(filepath, text):
    """
    Writes the given text to the specified file.

    :param filepath: The path to the file.
    :param text: The text to be written.
    """
    try:
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(text)
    except Exception as e:
        print(f"Error writing to file: {e}")
