import sys
input = sys.stdin.readline

li = [0] * 1001 # 자연수는 1000 까지
nums = [i*(i+1)//2 for i in range(1,45)] # i가 44일때 990으로 1000이하의 수 중 최대

for i in nums:
    for j in nums:
        for k in nums:
            if i+j+k <= 1000:
                li[i+j+k] = 1

for _ in range(int(input())):
    print(li[int(input())])

    