class Storage:
    def __init__(self, stacks=None):
        if stacks is None:
            stacks = []
        self.stacks = stacks

    def get_height(self):
        return max([len(stack) for stack in self.stacks])

    def move_9000(self, amount, from_stack, to_stack):
        for i in range(amount):
            self.stacks[to_stack-1].append(self.stacks[from_stack-1].pop())

    def move_9001(self, amount, from_stack, to_stack):
        crates = list()
        for i in range(amount):
            crates.append(self.stacks[from_stack-1].pop())
        crates.reverse()
        self.stacks[to_stack-1].crates += crates

    def __str__(self):
        output = ""
        current_height = self.get_height()
        while current_height > 0:
            for stack in self.stacks:
                if len(stack) < current_height:
                    output += "   "
                else:
                    output += "[" + str(stack.crates[current_height-1]) + "]"

            current_height -= 1
            output += "\n"
        for i in range(1, len(self.stacks)+1):
            output += " " + str(i) + " "

        return output

    def get_top_row(self):
        output = ""
        for stack in self.stacks:
            output += stack.crates[-1]
        return output


class Stack:
    def __init__(self, crates=None):
        if crates is None:
            crates = []
        self.crates = crates

    def __str__(self):
        output = ""
        for crate in self.crates:
            output += "[" + str(crate) + "]"
        return output

    def __len__(self):
        return len(self.crates)

    def append(self, crate):
        self.crates.append(crate)

    def pop(self):
        return self.crates.pop()


def main():
    with open("input.txt", "r") as file:
        data = list()
        for line in file.readlines():
            x = line.replace("    ", " / ").replace("[", "").replace("]", "").strip().split(" ")
            y = [i for i in x if i]
            data.append(y)

    storage_a = Storage()
    storage_b = Storage()
    for i in range(len(data[0])):
        storage_a.stacks.append(Stack())
        storage_b.stacks.append(Stack())

    data_iter = iter(data)

    mode = "storage"
    for line in data_iter:
        stack_index = 0
        if line[0].isdigit():
            mode = "moves"
            next(data_iter)
            continue
            # print(line)
        if mode == "storage":
            for crate in line:
                if crate != "/":
                    storage_a.stacks[stack_index].crates.insert(0, crate)
                    storage_b.stacks[stack_index].crates.insert(0, crate)
                stack_index += 1
        else:
            storage_a.move_9000(int(line[1]), int(line[3]), int(line[5]))
            storage_b.move_9001(int(line[1]), int(line[3]), int(line[5]))

    print("storage_a:\n", storage_a, sep="")
    print("storage_b:\n", storage_b, sep="")

    print("a:", storage_a.get_top_row())
    print("b:", storage_b.get_top_row())


if __name__ == "__main__":
    main()