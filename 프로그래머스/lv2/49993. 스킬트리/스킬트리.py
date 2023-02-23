def solution(skill, skill_trees):
    answer = 0
    for s in skill_trees:
        check = ""
        for i in s:
            if i in skill:
                check += i
        
        if skill.startswith(check):
            answer+=1
        
    return answer