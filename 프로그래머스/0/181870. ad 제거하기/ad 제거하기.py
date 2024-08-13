def solution(strArr):
    answer = []
    
    for item in strArr:
        if "ad" not in item:
            answer.append(item)
            
    return answer