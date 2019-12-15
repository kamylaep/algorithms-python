def findmostsimilarword(typed_word, option_a, option_b):
    op_a = __calcpossibilities__(typed_word, option_a)
    op_b = __calcpossibilities__(typed_word, option_b)

    return option_a if op_a > op_b else option_b


def __calcpossibilities__(typed_word, option):
    grid = [[0] * len(option) for i in range(len(typed_word))]

    grid_len = len(grid)

    for x in range(grid_len):
        for y in range(len(grid[x])):
            x_aux = x if x == 0 else x - 1
            y_aux = y if y == 0 else y - 1

            if typed_word[x] == option[y]:
                grid[x][y] = grid[x_aux][y_aux] + 1
            else:
                grid[x][y] = max((grid[x_aux][y], grid[x][y_aux],))

    # print(grid)
    return grid[grid_len - 1][grid_len - 1]
