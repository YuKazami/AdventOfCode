import sys

from Filesystem import Filesystem

class Buffer:
    def __init__(self, size: int, unique: bool):
        self.items = []
        self.size = size

    def add(self, item) -> bool:
        if len(self.items) < self.size:
            self.items.append(item)
        else:
            if len(self.items) == len(set(self.items)):
                return False
            self.items.pop(0)
            self.items.append(item)

        return True


def main():
    with open("input.txt", "r") as file:
        filesystem = Filesystem.import_from_terminal(file.read())

        print("a:", filesystem.get_limited_size(100000))
        print("b:", filesystem.find_dir_to_free_up(70000000, 30000000).get_size())

if __name__ == "__main__":
    main()