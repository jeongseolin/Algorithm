def solution(numbers):
    answer = []
    sum = 0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            sum = numbers[i] + numbers[j]
            if sum not in answer:
                answer.append(sum)
    answer.sort()
    return answer