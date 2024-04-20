import os.path
from prettytable import PrettyTable


class UI:

    def get_file_path(self):
        filename = input("Give name of the file (e.g. sample.txt): ")
        if os.path.isfile(f"src/{filename}"):
            return f"src/{filename}"
        return None

    def get_algorithm(self):
        print("\nChoose one algorithm or both")
        algorithm = input(
            "Press H: Huffman coding\nPress L: LZW\nPress C: Compare both\nPress E: Exit\n").upper()
        return algorithm

    def get_action(self):
        print("\nChoose action")
        action = input(
            "Press C: Compress \npress D: Decompress\npress E: Exit\n").upper()
        return action

    def display_message(self, message):
        print(message)

    def display_table(self, compression_stats):
        table = PrettyTable()
        table.field_names = ["Algorithm", "Compression time",
                             "Decompression time", "Compression ratio"]

        for stats in compression_stats:
            if stats is not None:
                table.add_row(stats)
        print(str(table))
