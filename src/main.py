import huffman


def huffman_coding(filename):

    huffman_algorithm = huffman.HuffmanCoding(f"src/{filename}")
    while True:
        action = input(
            "Press C: compress \npress D: decompress\npress E: exit\n").upper()
        if action == "C":
            huffman_algorithm.compress()
            print("Compressed")
        if action == "D":
            huffman_algorithm.decompress()
            print("Decompressed")
        if action == "E":
            break


def main():
    filename = input("Give name of the file ")
    while True:
        algorithm = input(
            "Press H to Huffman coding and press E to exit: ").upper()
        if algorithm == "H":
            huffman_coding(filename)
        if algorithm == "E":
            break


H = huffman.HuffmanCoding("src/text.txt")
H.compress()
H.decompress()
# main()
