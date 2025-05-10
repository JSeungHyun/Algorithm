def solution():
    N = int(input())
    items = sorted(list(map(int, input().split())))
    result = 0

    if N < 3:
        print(0)
        return
    
    for i in range(N):
        target = items[i]
        left = 0
        right = N - 1

        while left < right:
            # 자기 자신은 제외하기
            if left == i:
                left += 1
                continue
            if right == i:
                right -= 1
                continue

            current_value = items[left] + items[right]
            if target == current_value:
                result += 1
                break
            elif target > current_value:
                left += 1
            else:
                right -= 1
    
    print(result)

solution()