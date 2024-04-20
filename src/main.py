from compression_comparator import CompressionComparator
from filehandler import FileHandler
from huffman import HuffmanCoding
from lzw import LZW
from ui import UI


def action_loop(ui, comparator, algorithm, prev_compress=False):
    while True:
        action = ui.get_action()
        if action == "C":
            comparator.compress(algorithm)
            prev_compress = True
            ui.display_message("Compressed")
        if action == "D":
            if prev_compress:
                comparator.decompress(algorithm)
                ui.display_message("Decompressed")
            else:
                ui.display_message("File must be compressed first")
        if action == "E":
            break

def main():
    ui = UI()
    while True:
        path = ui.get_file_path()
        if path:
            filehandler = FileHandler(path)
            break
        ui.display_message("File not found")

    huffman = HuffmanCoding()
    lzw = LZW()
    comparator = CompressionComparator(filehandler)

    while True:
        chosen_algorithm = ui.get_algorithm()
        if chosen_algorithm == "H":
            action_loop(ui, comparator, huffman)
        if chosen_algorithm == "L":
            action_loop(ui, comparator, lzw)
        if chosen_algorithm == "C":
            ui.display_message("\nCalculating...")
            ui.display_table(comparator.compare(huffman, lzw))
            break
        if chosen_algorithm == "E":
            break


main()
