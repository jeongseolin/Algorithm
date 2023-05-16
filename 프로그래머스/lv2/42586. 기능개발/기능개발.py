def solution(progresses, speeds):
    answer = []
    play = 0
    develop = 0
    
    while len(progresses) > 0:
        if progresses[0] + play * speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            develop += 1
        else :
            if develop > 0:
                answer.append(develop)
                develop = 0
            play += 1
    answer.append(develop)
    return answer