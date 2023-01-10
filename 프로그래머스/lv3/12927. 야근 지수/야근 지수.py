import heapq
def solution(n, works):
    answer = 0
    heap = []
    
    for work in works:
        heapq.heappush(heap,-work)
    while n != 0:
        n -= 1
        heapq.heappush(heap,heapq.heappop(heap)+1)
    if -heap[0] <= 0:
        return 0
    else:
        for i in heap:
            answer += i ** 2
        return answer