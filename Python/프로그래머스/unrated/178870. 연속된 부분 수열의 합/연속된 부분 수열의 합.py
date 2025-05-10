def solution(sequence, k):
    l = len(sequence)
    answer = [0, 100000000000]
    end = 0
    total = sequence[0]
    
    for start in range(l):
        while end < l - 1 and total < k:
            end += 1
            total += sequence[end]
            
        if total == k:
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
        
        total -= sequence[start]
    
    return answer