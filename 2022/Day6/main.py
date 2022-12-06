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
        for line in file.readlines():
            buffer_a = Buffer(4, True)
            buffer_b = Buffer(14, True)
            processed_chars_a = 0
            for char in line:
                if not buffer_a.add(char):
                    break
                processed_chars_a += 1

            processed_chars_b = 0
            while buffer_b.add(line[processed_chars_b]):
                processed_chars_b += 1

    print("a:", processed_chars_a)
    print("b:", processed_chars_b)



if __name__ == "__main__":
    main()