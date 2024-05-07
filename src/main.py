import sys
from compression_comparator import CompressionComparator
from utilities.filehandler import FileHandler
from algorithms.huffman import HuffmanCoding
from algorithms.lzw import LZW
from ui import UI


def action_loop(ui, comparator, algorithm, table):
    """Choose action in a loop.

    This method will call the UI to choose the action:
    - If "C": Compress the file with given algorithm and update the table.
    - If "D": Decompress the file with given algorithm  (only if the file has been
      compressed previously). Update the column of the decompression time to the table.
    - If "E": the loop breaks.

    Args:
        ui (UI): An instance of the user interface.
        comparator (CompressionComparator): A comparator object to process the compression
                                        and decompression.
        algorithm (HuffmanCoding or LZW): An algorithm object (HuffmanCoding or LZW).
        table (list): A list containing the compression statistics for each algorithm.
                    Each list element is a list with the format [algorithm name, filename,
                    filesize, compressed filesize, compression ratio, compression time,
                    decompression time
    """

    while True:

        action = ui.choose_action()
        if action == "C":
            ui.display_message("Compressing...")
            stats = comparator.benchmark_compress(algorithm)
            update_table(table, stats)
            ui.display_table(table)

        if action == "D":
            if algorithm.prev_compress:
                ui.display_message("Decompressing...")
                stats = comparator.benchmark_decompress(algorithm)
                update_table(table, stats)
                ui.display_table(table)

            else:
                ui.display_message("File must be compressed first.")
        if action == "E":
            break


def create_filehandler(ui):
    """Create a FileHandler instance.

    This method prompts the UI to choose a file from a list of available files and creates a new
    instance of FileHandler, which is responsible for handling the chosen file.

    Args:
        ui (UI): An instance of the user interface.

    Returns:
        filehandler (FileHandler): An instance of FileHandler, which handles the chosen file.
    """
    filename = ui.choose_file()
    filehandler = FileHandler(filename)
    return filehandler


def choose_algorithm_loop(ui, comparator):
    """Choose algorithm in a loop.

    This method will create the instances of HuffmanCoding and LZW algorithms and initializes
    an empty table to store the compression results.

    The user is prompted to choose an action:
    - If "H" or "L", this method calls the action loop with the corresponding algorithm.
    - If "C", the comparator is invoked to compare both algorithms
      and display the results to the user.
    - If "E", the loop breaks.

    Args:
        ui (UI): An instance of the user interface.
        comparator (CompressionComparator): An instance of the CompressionComparator responsible
                                            for compression and decompression processing.


    """
    huffman = HuffmanCoding()
    lzw = LZW()
    table = []
    while True:
        print(f"Chosen file: {comparator.filehandler.filename}")
        chosen_algorithm = ui.choose_algorithm()
        if chosen_algorithm == "H":
            action_loop(ui, comparator, huffman, table)
        if chosen_algorithm == "L":
            action_loop(ui, comparator, lzw, table)
        if chosen_algorithm == "C":
            ui.display_message("\nCalculating...")
            ui.display_table(comparator.compare(huffman, lzw))
            break
        if chosen_algorithm == "E":
            break


def update_table(statistics_table, new_stats):
    """Update the table with the new statistics.

    This method uses the next function to find the first row in the table that matches the algorithm
    name.
    - If a match is found, it updates the row with the new statistics.
    - If no match is found, a StopIteration exeption is catched and the new row is appended
    to the table.

    Args:
        table (list): The table to store the statistics.
        stats (list): The row containing the new statistics to be updated or added to the table.
    """
    algorithm_name = new_stats[0]
    try:
        row = next(row for row in statistics_table if row[0] == algorithm_name)
        for i in range(4, len(row)):
            if new_stats[i] != 0:
                row[i] = new_stats[i]
    except StopIteration:
        statistics_table.append(new_stats)


def automatic_start():
    """Run the program automatically (non interactive mode).

    This method runs the compression and decompression algorithms automatically for all the non
    empty text files in the directory and display the results to the user.

    The process involves the following steps:
    1. Initialize the user interface.
    2. Get a list of all non empty text files in the directory.
    3. For each file:
        - Initialize HuffmanCoding and LZW compression algorithms.
        - Create a FileHandler instance for the file.
        - Initialize a CompressionComparator with the FileHandler.
        - Compare the performance of HuffmanCoding and LZW algorithms using the Comparator.
        - Store the results in a table.
        - Remove the temporary files.
    4. Display the compression statistics table to the user.

    """
    ui = UI()
    all_files = ui.list_non_empty_text_files()

    table = []
    ui.display_message("Calculating...")
    for file in all_files:
        huffman = HuffmanCoding()
        lzw = LZW()
        filename = file[1]
        filehandler = FileHandler(filename)
        comparator = CompressionComparator(filehandler)
        result = comparator.compare(huffman, lzw)
        table.extend(result)
        filehandler.tear_down()

    ui.display_table(table)


def start():
    """Run the program in the interactive mode.

    This method runs the program in interactive mode, where the user is prompted to enter
    a filename and choose algorithms and actions. The user will be guided through the process
    of choosing compression algorithms, performing compression and decompression actions,
    and viewing compression statistics.

    The interactive mode allows the user to:
    - Select the specific file to work on from the list.
    - Choose between different compression algorithms (Huffman Coding or LZW).
    - Perform compression and decompression actions on the chosen file.
    - View compression statistics.
    """
    ui = UI()
    filehandler = create_filehandler(ui)
    comparator = CompressionComparator(filehandler)
    choose_algorithm_loop(ui, comparator)
    filehandler.tear_down()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "start":
            start()
        elif sys.argv[1] == "automatic_start":
            automatic_start()
