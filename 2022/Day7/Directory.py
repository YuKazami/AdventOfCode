class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.children = {}
        self.parent = parent

    def get_dirs(self):
        dirs = []
        for child in self.children.values():
            if isinstance(child, Directory):
                dirs.append(child)
                dirs += child.get_dirs()
        return dirs

    def get_size(self) -> int:
        return sum(child.get_size() for child in self.children.values())

    def get_limited_size(self, limit: int) -> int:
        limited_sum = 0

        for child in self.children.values():
            if limited_sum + child.get_size() > limit:
                return limited_sum
            else:
                limited_sum += child.get_size()
