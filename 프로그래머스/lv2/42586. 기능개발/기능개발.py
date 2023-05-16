def solution(progresses, speeds):
    answer = []
    play = 0
    develop = 0
    
    while len(progresses) > 0:
        if progresses[0] + play * speeds[0] >= 100: #개발완료
            progresses.pop(0)
            speeds.pop(0)
            develop += 1
        else : #개발중
            play += 1
            if develop > 0: #이전에 기능이 개발되었다면
                answer.append(develop)
                develop = 0
    answer.append(develop)
    return answer