def solution(board):
    OX = {"O":0, "X":0, "completeO":0, "completeX":0}
    
    for b in board:
        countO = b.count("O")
        countX = b.count("X")
        OX["O"] += countO
        OX["X"] += countX
        # 가로로 완성된 경우
        if countO == 3: 
            OX["completeO"] += 1
        if countX == 3:
            OX["completeX"] += 1
        
    if OX["O"] < OX["X"] or OX["O"] >= OX["X"] + 2:  
        return 0
    
    if OX["O"] >= 3: # O가 3개 이상일 경우 완성된 갯수가 하나보다 크다면 성립 X
        # 세로로 완성된 경우
        if board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
            OX["completeX"] += 1
        if board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
            OX["completeX"] += 1    
        if board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
            OX["completeX"] += 1
        if board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
            OX["completeO"] += 1
        if board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
            OX["completeO"] += 1    
        if board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
            OX["completeO"] += 1
        # 대각선으로 완성된 경우
        if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
            OX["completeX"] += 1
        if board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
            OX["completeO"] += 1
        if board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
            OX["completeX"] += 1
        if board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
            OX["completeO"] += 1
            
    if OX["completeX"] >= 1 and OX["completeO"] >= 1: # 둘 다 승리하는 경우
        return 0
    if OX["completeX"] == 1 or OX["completeX"] == 2: # X가 승리했는데 O의 개수와 다를 경우
        if OX["X"] != OX["O"]:
            return 0
    if OX["completeO"] == 1 or OX["completeO"] == 2:
        if OX["O"] <= OX["X"]:
            return 0
    return 1