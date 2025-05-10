def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(begin, end):
    answer = []
    for i in range(begin, end+1):
        k = 0
        if i == 1:
            answer.append(0)
            continue
        elif isPrime(i):
            k = 1
        else:
            for j in range(2, int(i**0.5)+1):
                if i % j == 0:                
                    if i // j <= 10 ** 7:
                        k = max(k, i // j)
                    else:
                        k = j
        answer.append(k)
    
    return answer