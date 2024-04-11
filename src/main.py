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
        if action == "D":
            if prev_compress:
                comparator.decompress(algorithm)
            else:
                ui.display_message("File must be compressed first")
        if action == "E":
            break

def main():
    ui = UI()
    path = ui.get_file_path()
    filehandler = FileHandler(path)
    huffman = HuffmanCoding(filehandler)
    lzw = LZW(filehandler)
    comparator = CompressionComparator(huffman, lzw)

    while True:
        chosen_algorithm = ui.get_algorithm()
        if chosen_algorithm == "H":
            action_loop(ui, comparator, huffman)
        if chosen_algorithm == "L":
            action_loop(ui, comparator, lzw)
        if chosen_algorithm == "E":
            break
main()
