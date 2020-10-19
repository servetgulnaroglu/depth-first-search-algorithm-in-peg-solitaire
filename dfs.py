import time
from collections import deque as queue

node_x = ["NORTH", "EAST", "SOUTH", "WEST"]
node_2x = ["NORTH", "EAST", "SOUTH", "WEST"]
horizontal = {"NORTH": 0, "EAST": 1, "SOUTH": 0, "WEST": -1}
vertical = {"NORTH": -1, "EAST": 0, "SOUTH": 1, "WEST": 0}

maximum_depth = 0
count = 0

board = [[1 for j in range(7)] for i in range(7)]
board[0][0] = -1
board[0][1] = -1
board[1][0] = -1
board[1][1] = -1
board[5][0] = -1
board[5][1] = -1
board[6][0] = -1
board[6][1] = -1
board[0][5] = -1
board[0][6] = -1
board[1][5] = -1
board[1][6] = -1
board[5][5] = -1
board[5][6] = -1
board[6][5] = -1
board[6][6] = -1
board[3][3] = 0


def dfs(board, pegs, row, col, st):
    global maximum_depth, count, node_x, horizontal, vertical

    check_board(board)
    #Time Check
    current_time = time.time()
    if (current_time - start_time >= limit_time):
        print("\nNo solution due to time limit")
        return True
    if (pegs < 1):
        print('\nNo solution found')
        return False

    if (pegs == 1 and board[3][3] == 1):
        print('\nSolution found')
        return True

    if (len(st) > maximum_depth):
        maximum_depth = len(st)

    count += 1

    while (len(st) > 0):
        current_time = time.time()
        if (current_time - start_time >= limit_time):
            print("\nNo solution due to time limit")
            return True
        grid = st[len(st) - 1]
        st.remove(st[len(st) - 1])
        x = grid[0]
        y = grid[1]
        if board[x][y] == 1:
            for direction in node_x:
                if move(board, x, y, direction) and board[x + horizontal[direction]][
                    y + vertical[direction]] == 1 and (
                        (x + horizontal[direction], y + vertical[direction]) not in st):
                    st.append((x + horizontal[direction], y + vertical[direction]))

                if jump(board, x, y, direction) and board[x + 2 * horizontal[direction]][
                    y + 2 * vertical[direction]] == 1 and (
                        (x + 2 * horizontal[direction], y + 2 * vertical[direction]) not in st):
                    st.append((x + 2 * horizontal[direction], y + 2 * vertical[direction]))

            for direction in node_x:
                if (move(board, x, y, direction) and jump(board, x, y, direction) and
                        board[x + horizontal[direction]][y + vertical[direction]] == 1 and
                        board[x + 2 * horizontal[direction]][y + 2 * vertical[direction]] == 0):
                    board[x][y] = 0
                    board[x + horizontal[direction]][y + vertical[direction]] = 0
                    board[x + 2 * horizontal[direction]][y + 2 * vertical[direction]] = 1

                    if dfs(board, pegs - 1, x + 2 * horizontal[direction], y + 2 * vertical[direction],
                                        st):
                        return True
    return False



def move(board, x, y, d):
    global horizontal
    global vertical
    return (x + horizontal[d] >= 0 and x + horizontal[d] < 7 and y + vertical[d] >= 0 and y + vertical[d] < 7 and board[x + horizontal[d]][y + vertical[d]] != -1)


def jump(board, x, y, d):
    global horizontal
    global vertical
    return (x + 2 * horizontal[d] >= 0 and x + 2 * horizontal[d] < 7 and y + 2 * vertical[d] >= 0 and y + 2 * vertical[d] < 7 and board[x + 2 * horizontal[d]][y + 2 * vertical[d]] != -1)


def check_board(board):
    print()
    for i in range(7):
        for j in range(7):
            if (board[i][j] == -1):
                print(" ", end=" ")
            else:
                print(board[i][j], end=" ")
        print()



start_time = time.time()
limit_time = int(input('\nSelect the time limit value as minutes: '))
limit_time = limit_time * 60

maximum_depth = 0
count = 0
print('\nDepth-First Search\nTime Limit:', limit_time // 60, 'Minutess')
store = []
store.append((3, 1))
dfs(board, 32, 3, 1, store)
current_time = time.time()
print('\nTime Spent', (current_time - start_time) / 60, 'Minutes', '\nNumber count:', count, '\nStored number in memory:', maximum_depth)

