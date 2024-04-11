import os.path
class UI:
      
    def get_file_path(self):
        filename = input("Give name of the file: ")
        if os.path.isfile(f"src/{filename}"):
            return f"src/{filename}"
    
    def get_algorithm(self):
        print("\nChoose algorithm")
        algorithm = input(
                    "Press H: Huffman coding\nPress L: LZW\nPress E: Exit\n").upper()
        return algorithm
    
    def get_action(self):
        print(f"\nChoose action")
        action = input(
            "Press C: Compress \npress D: Decompress\npress E: Exit\n").upper()
        return action
    
    def display_message(self, message):
        print(message)