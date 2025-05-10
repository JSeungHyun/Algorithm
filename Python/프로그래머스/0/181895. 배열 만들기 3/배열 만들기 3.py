def solution(arr, intervals):
    answer = []
    
    for s, e in intervals:
        answer.extend(arr[s : e + 1])
    
    return answer