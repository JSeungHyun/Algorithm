def dfs(board, n, row):
    res = 0
    if n == row:
        return 1
    for col in range(n):
        board[row] = col
        for i in range(row):
            if board[i] == board[row]: # 같은 열에 위치
                break
            if abs(board[i]-board[row]) == row - i: # 대각선에 위치
                break
        else:
            res += dfs(board, n, row+1)
    return res

def solution(n):
    return dfs([0] * n, n, 0)

