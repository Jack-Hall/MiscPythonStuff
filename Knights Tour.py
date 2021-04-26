def knightsTour(n):
    count = 0
    for i in range(n):
        for j in range(n):
            board = [[None for _ in range(n)] for _ in range(n)]
            board[i][j] = 0
            count += knightsTourHelper(board, [(i,j)], n)

    return count

def knightsTourHelper(board, tour, n):
    if len(tour) = n*n:
        return 1
    else:
        count = 0
        last_r, last_c = tour[-1]
        for r, c in validMoves(board, last_r, last_c, n):
            tour.append(r,c)
            board[r][c] = 0
            count += knightsTourHelper(board, tour, n)
            tour.pop()
            board[r][c] = None
        return count



def validMoves(board, r, c, n):
    deltas =[
        (2,   1),
        (-2,  1),
        (2,  -1),
        (-2,  1),
        (1,   2),
        (-1,  2),
        (1,  -2),
        (-1, -2)]
    allMoves = [r+ r_delta, c+ c_delta for r_delta, c_delta in deltas]
    return [move for move in allMoves if isValidMove(move, board, n)]

def isValidMove(move, board, n):
    r, c = move
    return 0 <= r < n and 0 <= c < n board[r][c] is None
