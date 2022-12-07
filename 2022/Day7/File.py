class File:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent

    def get_size(self) -> int:
        return self.size
