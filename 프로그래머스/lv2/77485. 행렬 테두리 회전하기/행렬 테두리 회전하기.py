import heapq
def solution(rows, columns, queries):
    graph = [[columns*j+i for i in range(1,columns+1)] for j in range(rows)]
    answer = []
    
    for y1,x1,y2,x2 in queries:
        heap = []
        
        # 1시 5시 7시 먼저 저장
        save = graph[y1-1][x1-1]
        save1 = graph[y1-1][x2-1]
        save2 = graph[y2-1][x2-1]
        save3 = graph[y2-1][x1-1]
        heapq.heappush(heap,save)
        heapq.heappush(heap,save1)
        heapq.heappush(heap,save2)
        heapq.heappush(heap,save3)
        
        # 상단 좌 -> 우
        for i in range(x2-1, x1-1, -1):
            graph[y1-1][i] = graph[y1-1][i-1]
            heapq.heappush(heap,graph[y1-1][i])
        
        # 우측 상 -> 하
        for i in range(y2-1, y1-1, -1):
            graph[i][x2-1] = graph[i-1][x2-1]
            heapq.heappush(heap,graph[i][x2-1])
        
    
        # 하단 우 -> 좌
        for i in range(x1-1,x2-1):
            graph[y2-1][i] = graph[y2-1][i+1]
            heapq.heappush(heap,graph[y2-1][i])
    
        
        # 좌측 하 -> 상
        for i in range(y1-1,y2-1):
            graph[i][x1-1] = graph[i+1][x1-1]
            heapq.heappush(heap,graph[i][x1-1])
            
        graph[y1][x2-1] = save1
        graph[y2-1][x2-2] = save2
        graph[y2-2][x1-1] = save3
        
        answer.append(heapq.heappop(heap))
    return answer