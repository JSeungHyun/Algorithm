import sys
input = sys.stdin.readline

N, M = map(int, input().split())
moneys = [int(input().rstrip()) for _ in range(N)]
result = sys.maxsize

def isValidMoney(money):
    if money < max(moneys):
        return False

    cnt = 1
    current_money = money

    for m in moneys:
        if current_money < m: # 금액이 작으면 인출
            cnt += 1
            current_money = money

            if cnt > M: # 인출 횟수가 커지면 유효하지 않음
                return False
            
        current_money -= m
    return True

left = max(moneys)
right = sum(moneys)
while left <= right:
    mid = (left + right) // 2
    if isValidMoney(mid):
        result = mid
        right = mid - 1
    else:
        left = mid + 1

print(result)