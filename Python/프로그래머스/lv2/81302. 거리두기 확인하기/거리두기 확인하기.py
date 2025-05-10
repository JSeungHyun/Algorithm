from collections import deque
def solution(places):
    answer = []
    board_size = 5
    dy = [0,0,-1,1]
    dx = [1,-1,0,0]
    
    def bfs(y,x,place):
        board = place[:]
        visited = [[False] * board_size for _ in range(board_size)]
        queue = deque([])
        queue.append((y,x,0))
        visited[y][x] = True
        while queue:
            y,x,distance = queue.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or nx < 0 or ny >= board_size or nx >= board_size:
                    continue
                elif board[ny][nx] == "P" and not visited[ny][nx]:
                    return False
                elif board[ny][nx] == "O" and distance < 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append((ny,nx,distance+1))
        return True
    
    for place in places:
        flag = False
        for y in range(board_size):
            if flag:
                break
            for x in range(board_size):
                if place[y][x] == "P":
                    if not bfs(y,x,place):
                        flag = True
                        break
        if flag:
            answer.append(0)
        else:
            answer.append(1)
        
    return answer