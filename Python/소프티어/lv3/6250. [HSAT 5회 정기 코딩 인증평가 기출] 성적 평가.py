import sys
input = sys.stdin.readline

N = int(input())
total_scores = [0] * N

def calculate_ranks(scores):
    score_groups = {}
    for idx, score in enumerate(scores):
        if score not in score_groups:
            score_groups[score] = []
        score_groups[score].append(idx)
    
    current_rank = 1
    ranks = [0] * N
    for score in sorted(score_groups.keys(), reverse=True):
        groups = score_groups[score]
        for idx in groups:
            ranks[idx] = current_rank
        current_rank += len(groups)
    return ranks

for _ in range(3):
    round_scores = list(map(int, input().split()))
    for i in range(N):
        total_scores[i] += round_scores[i]
    print(' '.join(map(str, calculate_ranks(round_scores))))

final_ranks = calculate_ranks(total_scores)
print(' '.join(map(str, final_ranks)))