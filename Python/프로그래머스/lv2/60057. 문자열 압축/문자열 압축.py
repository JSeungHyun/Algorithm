def solution(s):
    answer = len(s)
    for i in range(1,len(s)//2+1):
        comp = ""
        tmp = s[:i]
        cnt = 1
        for j in range(i,len(s),i):
            word = s[j:j+i]
            if word == tmp:
                cnt += 1
            else:
                if cnt >= 2:
                    comp += str(cnt)
                comp += tmp
                tmp = word
                cnt = 1
        if cnt >= 2:
            comp += str(cnt)
        comp += tmp
        answer = min(answer,len(comp))
    return answer