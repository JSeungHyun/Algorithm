import sys
input = sys.stdin.readline

a, b, dist = map(int, input().split())
result = 0

division_a = dist // a
mod_a = dist % a
division_b = dist // b
mod_b = dist % b

result += dist + (division_a * b if mod_a > 0 else (division_a - 1) * b)
result += dist + (division_b * a if mod_b > 0 else (division_b - 1) * a)

print(result)