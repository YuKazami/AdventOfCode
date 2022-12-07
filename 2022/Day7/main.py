from Filesystem import Filesystem


def main():
    with open("input.txt", "r") as file:
        filesystem = Filesystem.import_from_terminal(file.read())

        print("a:", filesystem.get_limited_size(100000))
        print("b:", filesystem.find_dir_to_free_up(70000000, 30000000).get_size())


if __name__ == "__main__":
    main()
