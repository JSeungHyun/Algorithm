import math
def solution(w,h):
    num = math.gcd(w,h)
    return w * h - (((h // num) + (w // num) - 1) * num)