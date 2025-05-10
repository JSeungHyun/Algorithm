import re
from itertools import permutations 

def solution(user_id, banned_id):
    banned_id = [i.replace("*", ".") for i in banned_id]
    answer = set()
    
    for i in permutations(user_id, len(banned_id)):
        lst = list(i)
        flag = True
        for j in range(len(banned_id)):
            if re.match(banned_id[j], lst[j]) and (len(banned_id[j]) == len(lst[j])) :
                continue 
            else:
                flag = False
                break
        if flag:
            answer.add("".join(sorted(lst)))

    return len(answer) 