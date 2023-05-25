def solution(todo_list, finished):
    answer = []
    for list, check in zip(todo_list, finished):
        if not check:
            answer.append(list)
    return answer