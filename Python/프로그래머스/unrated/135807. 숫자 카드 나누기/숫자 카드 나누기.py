def divisor(n):
    div = []
    for i in range(2,n//2+1):
        if n % i == 0:
            div.append(i)
    div.append(n)
    return div

def find(nums,arrA,arrB):
    res = 0
    for i in nums:
        for j in range(len(arrA)):
            if arrA[j] % i == 0 and arrB[j] % i != 0:
                continue
            break
        else:
            res = max(res,i)
    return res

def solution(arrayA, arrayB):
    minA = sorted(arrayA)[0]
    minB = sorted(arrayB)[0]
    answer = max(find(divisor(minA),arrayA,arrayB),find(divisor(minB),arrayB,arrayA))
    
    return answer