def dateCal(d1,d2):
    days = 0
    d1 = d1.split('.')
    d2 = d2.split('.')
    days += (int(d1[0]) - int(d2[0])) * 12 # 연의 차이
    days += int(d1[1]) - int(d2[1]) # 월의 차이
    days += (int(d1[2]) - int(d2[2])) / 28 # 일의차이
    
    return days

def solution(today, terms, privacies):
    answer = []
    term = {}
    # 유효기간 딕셔너리로 저장
    for i in terms:
        i = i.split()
        term[i[0]] = int(i[-1])
    for idx,i in enumerate(privacies):
        diff = dateCal(today,i[:-2])
        if term[i[-1]] <= diff:
            answer.append(idx+1)
    
    return answer
    
