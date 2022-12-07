from Directory import Directory
from File import File


class Filesystem:
    def __init__(self, root):
        self.root = root

    def get_dirs(self):
        dirs = []
        for child in self.root.children.values():
            if isinstance(child, Directory):
                dirs.append(child)
                dirs += child.get_dirs()
        return dirs

    def get_size(self) -> int:
        return sum(child.get_size() for child in self.root.children.values())

    def get_limited_size(self, limit: int) -> int:
        limited_sum = 0
        dirs = self.get_dirs()
        for child in dirs:
            if child.get_size() > limit:
                continue
            else:
                limited_sum += child.get_size()
        return limited_sum

    def find_dir_to_free_up(self, max_space, required_space):
        used_space = self.get_size()
        unused_space = max_space - used_space
        space_to_free = required_space - unused_space
        smallest_candidate = None
        if required_space <= unused_space:
            return 0
        else:
            for child in self.get_dirs():
                size = child.get_size()
                if size > space_to_free:
                    if smallest_candidate:
                        if size < smallest_candidate.get_size():
                            smallest_candidate = child
                    else:
                        smallest_candidate = child

            return smallest_candidate

    @classmethod
    def import_from_terminal(cls, terminal: str):
        root = Directory("/")
        terminal_iter = iter(terminal.splitlines())

        if next(terminal_iter) != "$ cd /":
            raise ValueError("Invalid terminal start")

        current_dir = root
        for line in terminal_iter:
            if line.startswith("$ ls"):
                ls_line = next(terminal_iter)

                while not ls_line.startswith("$"):
                    if ls_line.startswith("dir"):
                        dir_name = ls_line.split()[1]
                        current_dir.children[dir_name] = Directory(dir_name, current_dir)
                    else:
                        file_size, file_name = ls_line.split()
                        current_dir.children[file_name] = File(file_name, int(file_size), current_dir)

                    try:
                        ls_line = next(terminal_iter)
                    except StopIteration:
                        return cls(root)

                line = ls_line

            if line.startswith("$ cd"):
                target_name = line.split()[2]
                if target_name == "..":
                    current_dir = current_dir.parent
                else:
                    current_dir = current_dir.children[target_name]

            # print(current_dir.name)
