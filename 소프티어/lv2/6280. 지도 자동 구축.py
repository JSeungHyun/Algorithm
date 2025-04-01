import sys
input = sys.stdin.readline

n = int(input())
nums = [2]

for i in range(1, n+1):
    nums.append(2 * nums[i-1] - 1)

print(nums[n] ** 2)