import sys

input = sys.stdin.readline  # 빠른 입력을 위해 사용

# 입력 받기
H, W = map(int, input().split())
blocks = list(map(int, input().split()))

# 빗물 계산 로직 시작
total_volume = 0  # 총 빗물의 양 초기화
left = 0          # 왼쪽 포인터 초기화
right = W - 1     # 오른쪽 포인터 초기화 (배열 길이 - 1)
left_max = 0      # 왼쪽 포인터가 이동하면서 만난 최대 높이
right_max = 0     # 오른쪽 포인터가 이동하면서 만난 최대 높이

# 왼쪽 포인터가 오른쪽 포인터보다 왼쪽에 있는 동안 반복
while left < right:
    # 왼쪽 블록 높이가 오른쪽 블록 높이보다 낮은 경우
    if blocks[left] < blocks[right]:
        # 현재 왼쪽 블록 높이가 이전에 기록된 왼쪽 최대 높이보다 크면 갱신
        if blocks[left] > left_max:
            left_max = blocks[left]
        # 그렇지 않다면, 현재 왼쪽 블록 위에는 왼쪽 최대 높이만큼 물이 찰 수 있음
        else:
            total_volume += left_max - blocks[left]
        # 왼쪽 포인터를 오른쪽으로 한 칸 이동
        left += 1
    # 오른쪽 블록 높이가 왼쪽 블록 높이보다 크거나 같은 경우
    else:
        # 현재 오른쪽 블록 높이가 이전에 기록된 오른쪽 최대 높이보다 크면 갱신
        if blocks[right] > right_max:
            right_max = blocks[right]
        # 그렇지 않다면, 현재 오른쪽 블록 위에는 오른쪽 최대 높이만큼 물이 찰 수 있음
        else:
            total_volume += right_max - blocks[right]
        # 오른쪽 포인터를 왼쪽으로 한 칸 이동
        right -= 1

# 계산된 총 빗물의 양 출력
print(total_volume)