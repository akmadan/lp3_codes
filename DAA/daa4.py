global N
N = 4
cols = set([i for i in range(N)])
print(cols) # {0, 1, 2, 3}

# if user enters 0 1 then 1 will be removed from this set = {0,2,3} = cols


def printSolution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()


def isSafe(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    i, j = row + 1, col + 1
    while i < N and j < N:
        if board[i][j] == 1:
            return False
        i += 1
        j += 1
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i, j = row + 1, col - 1
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True


def solveNQUtil(board):

    # if no column in cols left
    if not cols:
        return True

    # set cols --> list cols[0]
    col = list(cols)[0]
    print(col)
    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            cols.remove(col)
            if solveNQUtil(board) == True:
                return True
            cols.add(col)
            board[i][col] = 0
    return False


def solveNQ():
    board = []
    for i in range(N):
        temp = []
        for j in range(N):
            temp.append(0)
        board.append(temp)
    i, j = input("Enter i, j position of first queen : ").split()
    i, j = int(i), int(j)
    board[i][j] = 1
    cols.remove(j)
    
    if solveNQUtil(board) == False:
        print("Solution does not exist")
        return False

    printSolution(board)
    return True


solveNQ()
