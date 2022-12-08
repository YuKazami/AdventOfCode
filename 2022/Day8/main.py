import numpy as np


def visibility(x, y, tree_grid, tree_visibility_grid, reversed=False, transposed=False):
    rx, ry = range(x), range(y)
    if reversed:
        ry = range(y-1, -1, -1)
    if transposed:
        for col in rx:
            highest_tree = -1
            for row in ry:
                tree = tree_grid[row][col]
                if tree > highest_tree:
                    highest_tree = tree
                    tree_visibility_grid[row][col] = True
    else:
        for row in rx:
            highest_tree = -1
            for col in ry:
                tree = tree_grid[row][col]
                if tree > highest_tree:
                    highest_tree = tree
                    tree_visibility_grid[row][col] = True


def scenic_score(x, y, tree_grid, tree_scenic_score_grid):
    def inner_loop(iview, rmod, cmod):
        iview += 1
        tree = tree_grid[row][col]
        if tree <= tree_grid[row + rmod][col + cmod]:
            tree_scenic_score_grid[row][col] *= 1
            blocking_trees.append((tree_grid[row + rmod][col + cmod], iview-1))
        else:  # bigger than neighbor
            for block in sorted(blocking_trees):
                if block[0] >= tree:  # smaller/eq than block
                    tree_scenic_score_grid[row][col] *= abs(iview - block[1])
                    break
            else:
                tree_scenic_score_grid[row][col] *= iview

        return iview

    # left -> right
    for row in range(1, x-1):  # skip last, because its a border
        view = 0
        blocking_trees = []
        for col in range(1, y-1):
            view = inner_loop(view, 0, -1)

    # right -> left
    for row in range(1, x-1):  # skip last, because its a border
        view = 0
        blocking_trees = []
        for col in range(y-2, 0, -1):
            view = inner_loop(view, 0, 1)

    # top -> bottom
    for col in range(1, y - 1):  # skip last, because its a border
        view = 0
        blocking_trees = []
        for row in range(1, x-1):
            view = inner_loop(view, -1, 0)

    # bottom -> top
    for col in range(1, y - 1):  # skip last, because its a border
        view = 0
        blocking_trees = []
        for row in range(x-2, 0, -1):
            view = inner_loop(view, 1, 0)

    print(tree_scenic_score_grid)


def scenic_score_brute(x, y, tree_grid, tree_scenic_score_grid):
    for row in range(x):  # skip last, because its a border
        for col in range(y):
            L = 0
            tree = tree_grid[row][col]
            for yi in range(col+1, y):
                L += 1
                if tree <= tree_grid[row][yi]:
                    break

            R = 0
            for yi in range(col-1, -1, -1):
                R += 1
                if tree <= tree_grid[row][yi]:
                    break

            D = 0
            for xi in range(row+1, x):
                D += 1
                if tree <= tree_grid[xi][col]:
                    break

            U = 0
            for xi in range(row-1, -1, -1):
                U += 1
                if tree <= tree_grid[xi][col]:
                    break

            print(L, R, D, U)
            tree_scenic_score_grid[row][col] *= L * R * D * U

    print(tree_scenic_score_grid)

def main():
    tree_grid = np.genfromtxt('input.txt', dtype=int, delimiter=1)

    tree_visibility_grid = np.zeros_like(tree_grid, dtype=bool)
    x, y = tree_grid.shape
    # left -> right
    visibility(x, y, tree_grid, tree_visibility_grid)

    # right -> left
    visibility(x, y, tree_grid, tree_visibility_grid, reversed=True)

    # top -> bottom
    visibility(x, y, tree_grid, tree_visibility_grid, transposed=True)

    # bottom -> top
    visibility(x, y, tree_grid, tree_visibility_grid, reversed=True, transposed=True)

    print("a:", np.sum(tree_visibility_grid))

    tree_scenic_score_grid = np.pad(np.ones((tree_grid.shape[0]-2, tree_grid.shape[1]-2), dtype=int), pad_width=1, mode='constant', constant_values=0)

    scenic_score_brute(x, y, tree_grid, tree_scenic_score_grid)

    print("b:", tree_scenic_score_grid.max())


if __name__ == "__main__":
    main()
