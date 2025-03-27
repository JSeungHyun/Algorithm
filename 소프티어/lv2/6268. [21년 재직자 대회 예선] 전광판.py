import sys
input = sys.stdin.readline

def count_differences(array1, array2):
    return sum(a != b for a, b in zip(array1, array2))

lights = {}
lights[None] = [0, 0, 0, 0, 0, 0, 0]
lights[0] = [1, 1, 1, 0, 1, 1, 1]
lights[1] = [0, 0, 1, 0, 0, 1, 0]
lights[2] = [1, 0, 1, 1, 1, 0, 1]
lights[3] = [1, 0, 1, 1, 0, 1, 1]
lights[4] = [0, 1, 1, 1, 0, 1, 0]
lights[5] = [1, 1, 0, 1, 0, 1, 1]
lights[6] = [1, 1, 0, 1, 1, 1, 1]
lights[7] = [1, 1, 1, 0, 0, 1, 0]
lights[8] = [1, 1, 1, 1, 1, 1, 1]
lights[9] = [1, 1, 1, 1, 0, 1, 1]

for _ in range(int(input())):
    num1, num2 = input().split()
    num1_len = len(num1)
    num2_len = len(num2)
    max_length = max(num1_len, num2_len)

    list1 = [None] * (max_length - num1_len) + list(map(int, num1))
    list2 = [None] * (max_length - num2_len) + list(map(int, num2))

    result = 0
    for i in range(max_length):
        result += count_differences(lights[list1[i]], lights[list2[i]])
    print(result)