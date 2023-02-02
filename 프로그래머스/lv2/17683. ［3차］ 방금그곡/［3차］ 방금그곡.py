import math
#시간 차이 구하기
def checkTime(t1,t2): 
    t1_h,t1_m = t1.split(":")
    t2_h,t2_m = t2.split(":")
    return ((int(t2_h) * 60) + int(t2_m)) - ((int(t1_h) * 60) + int(t1_m))
    
def solution(m, musicinfos):
    answer = ''
    highCode = {"A#":'a',"C#":'c',"D#":'d',"F#":'f',"G#":'g'} # #음을 바꾸기
    playList = []
    for h in highCode:
        m = m.replace(h,highCode[h]) # m에서 #음 치환
        
    for i in musicinfos:
        s,e,name,play = i.split(',')
        for h in highCode:
            play = play.replace(h,highCode[h]) # 재생목록에서 #음 치환
        c = checkTime(s,e)
        playList.append([(play*(math.ceil(c / len(play))))[:c],name]) #시간까지의 음과 이름 추가
    
    playList.sort(key=lambda x:(-len(x[0]))) # 재생시간순으로 정렬
    for i in playList:
        if m in i[0]:
            return i[1]
    return "(None)"