from itertools import combinations
def solution(orders, course):
    orders = [''.join(sorted(i)) for i in orders]
    answer = []
    for i in course:
        dict = {}
        for j in orders:
            s = combinations(j,i)
            for k in sorted(s):
                k = ''.join(list(k))
                if k in dict:
                    dict[k] += 1
                else:
                    dict[k] = 1
        maxValue = max(dict.values()) if dict.values() else 0
        for a,b in sorted(dict.items(),key=lambda x:-x[1]):
            if b == maxValue and b > 1:
                answer.append(a)
            else:
                break
    return sorted(answer)