import sys
input = sys.stdin.readline

N = int(input())
total_score = [0] * N

for _ in range(N):
    items = list(map(int, input().split()))
    ranks_dict = {}
    for i, v in enumerate(items):
        total_score[i] += v
        if v in ranks_dict:
            ranks_dict[v].append(i)
        else:
            ranks_dict[v] = [i]
    
    rank = 1
    ranks_list = [0] * N
    for key in sorted(ranks_dict.keys(), reverse=True):
        ranks = ranks_dict[key]
        for r in ranks:
            ranks_list[r] = rank
        rank += len(ranks)
    print(' '.join(map(str, ranks_list)))

ranks_dict = {}
for i, v in enumerate(total_score):
    if v in ranks_dict:
        ranks_dict[v].append(i)
    else:
        ranks_dict[v] = [i]

rank = 1
ranks_list = [0] * N
for key in sorted(ranks_dict.keys(), reverse=True):
    ranks = ranks_dict[key]
    for r in ranks:
        ranks_list[r] = rank
    rank += len(ranks)
print(' '.join(map(str, ranks_list)))