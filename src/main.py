import huffman


def huffman_coding(filename):
    prev_compress = False

    huffman_algorithm = huffman.HuffmanCoding(f"src/{filename}")
    while True:
        action = input(
            "Press C: compress \npress D: decompress\npress E: exit\n").upper()
        if action == "C":
            huffman_algorithm.compress()
            print("Compressed")
            prev_compress = True
        if action == "D":
            if prev_compress:
                huffman_algorithm.decompress()
                print("Decompressed")
            else:
                print("File must be first compressed")
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


main()
