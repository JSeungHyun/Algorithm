import heapq
def solution(n, works):
    answer = 0
    heap = []
    
    for work in works:
        heapq.heappush(heap,-work)
    while n != 0:
        n -= 1
        heapq.heappush(heap,heapq.heappop(heap)+1)
    
    return sum([i**2 for i in heap if i <= 0])