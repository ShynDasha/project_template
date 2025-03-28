from app.io import output
from app.io import input



def main():
    """
    Main function that reads input from different sources, prints the results to the console,
    and writes them to an output file.
    """
    # Read text from the console
    text_console = input.read_from_console()

    # Read from a file using built-in Python functions
    text_file = input.read_from_file("data/input.txt")

    # Read from a file using pandas
    text_pandas = input.read_from_file_pandas("data/input.txt")

    # Print results to the console
    output.write_to_console("Text from console:\n" + text_console)
    output.write_to_console("Text from file:\n" + text_file)
    output.write_to_console("Text from file (pandas):\n" + text_pandas)

    # Write results to a file
    output.write_to_file("data/output.txt", f"Text from console:\n{text_console}\n\n"
                                            f"Text from file:\n{text_file}\n\n"
                                            f"Text from file (pandas):\n{text_pandas}\n")


if __name__ == "__main__":
    main()
