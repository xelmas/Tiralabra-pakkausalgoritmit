import os.path
from prettytable import PrettyTable
from utilities.utils import FILE_DIRECTORY


class UI:

    def display_files(self, text_files):
        """Display all text files from the textfiles-directory to the user.

        Args:
            text_files (list): A list containing the file info for each file element.
                            Each list element is a list with the format [number, filename, size].
        """
        table = PrettyTable()
        table.field_names = ["Number", "Name", "Size (kB)"]
        table.float_format = ".3"

        for file_info in text_files:
            table.add_row(file_info)

        print(str(table))

    def list_non_empty_text_files(self):
        """Create a list of text files that can be compressed.

        This method will go through all the files from the directory with the extension ".txt"
        and adds the file to the list if its not empty.

        Returns:
            text_files (list): A list containing the file info for each file. Each list
                            element is a list with the format [number, filename, filesize].
        """
        text_files = []
        number = 0
        for filename in os.listdir(FILE_DIRECTORY):
            if filename.endswith(".txt"):
                file_path = os.path.join(FILE_DIRECTORY, filename)
                size = os.path.getsize(file_path) / 1024
                if size > 0:
                    number += 1
                    text_file = [number, filename, size]
                    text_files.append(text_file)

        return text_files

    def choose_file(self):
        """Choose a file to be compressed/decompressed.

        This method prints all the available files to the user and waits for the input.
        If the input is a valid number, filename of the chosen file is returned.
        If the input is not valid, the user will be asked to enter the input again.

        Returns:
            filename (str): A filename of the chosen file.
        """
        print("\nAvailable files:")
        text_files = self.list_non_empty_text_files()
        self.display_files(text_files)

        while True:
            chosen_file = input("Choose a file by entering the number: ")
            if chosen_file.isdigit():
                chosen_file = int(chosen_file) - 1

                if 0 <= chosen_file < len(text_files):
                    filename = text_files[chosen_file][1]
                    return filename
                print("Invalid choice. Please enter a valid number.\n")
            else:
                print("Invalid input. Please enter a number.\n")

    def choose_algorithm(self):
        """Choose an algorithm to compress/decompress the file.

        This method prompts the user and waits for the input.
        If the input is:
        - H : Huffman coding
        - L : Lempel-Ziv-Welch
        - C : Compare both algorithms
        - E : Exit
        If the input is anything else, the user will be prompted again.

        Returns:
            algorithm (str): A character representing the chosen algorithm.
        """
        while True:
            print("\nChoose one algorithm or both")
            algorithm = input(
                "Press H: Huffman coding\n"
                "Press L: LZW\n"
                "Press C: Compare both\n"
                "Press E: Exit\n").upper()
            if algorithm in ["H", "L", "C", "E"]:
                return algorithm
            print("Invalid choice. Please enter a valid character.")

    def choose_action(self):
        """Choose to compress or decompress the file.

        This method prompts the user and waits for the input.

        Returns:
            action (str): A character representing the chosen action.
        """
        while True:
            print("\nChoose action")
            action = input(
                "Press C: Compress \n"
                "press D: Decompress\n"
                "press E: Exit\n").upper()
            if action in ["C", "D", "E"]:
                return action
            print("Invalid input. Please enter a valid character.")

    def display_message(self, message):
        """Print the message to the user.

        Args:
            message (str): A message to be printed to the console.
        """
        print(message)

    def has_none_value(self, compression_stats):
        """Check if any value in the compression stats list is None.

        Args:
            compression_stats (list): The values from the compression process.

        Returns:
            bool: If one or more value is None, returns True. Otherwise, False.
        """
        for value in compression_stats:
            if value is None:
                return True

        return False

    def display_table(self, compression_stats):
        """Print the table to the user.

        This method will create a prettyTable object that has field names
        Algorithm, Filename, Size, Compressed size, Compression ratio, Compression time,
        Decompression time. Each algorithm that has not any None values are added to the table
        as a row. If the algorithm has any None values, it is indicating a decompression error,
        and it will be printed to the console.

        Args:
            compression_stats (list): A list containing the compression statistics for each 
                                    algorithm. Each list element is a list with the format
                                    [algorithm name, filename, filesize, compressed filesize,
                                    compression ratio, compression time, decompression time]
        """
        table = PrettyTable()
        table.field_names = ["Algorithm", "Filename", "Size (kB)", "Compressed size (kB)",
                             "Compression ratio (%)", "Compression time (s)",
                             "Decompression time (s)"]
        table.float_format = ".4"

        for algorithm_stats in compression_stats:
            if algorithm_stats is not None:
                if self.has_none_value(algorithm_stats[3:]):
                    algorithm_name = algorithm_stats[0]
                    print(
                        f"Decompressed filesize differs from the original "
                        f"with algorithm {algorithm_name}.")
                table.add_row(algorithm_stats)
        print(str(table))
