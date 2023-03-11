from sudoku import *


def main():
    exit_condition1 = 0
    exit_condition2 = 0
    grid = grid_preset.copy()
    while True:
        for lkj in grid:
            for num in lkj:
                if num == 0:
                    for x in range(len(grid)):
                        for y in range(x):
                            if grid[x][y] == 0:
                                solution(grid, x, y)
                    break
                else:
                    exit_condition1 += 1
            if exit_condition1 == 9:
                exit_condition1 = 0
                exit_condition2 += 1
        if exit_condition2 == 9:
            print(grid)
            output(grid)
            exit(0)
        print("cycle done")
        


def solution(grid, x, y):
    poss = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # solucoes possiveis
    for num in grid[x]:
        if num != 0:
            poss.remove(num)
    for i in range(9):
        if grid[i][y] != 0 and grid[i][y] in poss:
            poss.remove(grid[i][y])
    square = check_square(x, y)
    if square < 4:
        dislocationx = 0
    elif square < 7:
        dislocationx = 3
    else:
        dislocationx = 6

    if square == 1 or square == 4 or square == 7:
        dislocationy = 0
    elif square == 2 or square == 5 or square == 8:
        dislocationy = 3
    else:
        dislocationy = 6
    for i in range(3):
        for h in range(3):
            if grid[i+dislocationx][h+dislocationy] != 0 and grid[i+dislocationx][h+dislocationy] in poss:
                poss.remove(grid[i+dislocationx][h+dislocationy])
    print(poss)
    if len(poss) == 1:
        grid[x][y] = poss[0]
        print("num written")


def check_square(y, x):  # 1  2  3
    if y < 3:            # 4  5  6
        if x < 3:        # 7  8  9
            return 1
        elif x < 6:
            return 2
        else:
            return 3
    elif y < 6:
        if x < 3:
            return 4
        elif x < 6:
            return 5
        else:
            return 6
    else:
        if x < 3:
            return 7
        elif x < 6:
            return 8
        else:
            return 9


if __name__ == "__main__":
    main()
