def solution(numbers):
    answer = [0] * len(numbers)
    answer[-1] = -1
    stack = [numbers[-1]]
    
    for i in reversed(range(len(numbers)-1)):
        number = numbers[i]
        while number >= stack[-1]:
            stack.pop()
            if not stack:
                break
        if stack:
            answer[i] = stack[-1]
        else:
            answer[i] = -1
        stack.append(number)
        
    return answer