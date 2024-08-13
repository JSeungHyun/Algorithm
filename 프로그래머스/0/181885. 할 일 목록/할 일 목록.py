def solution(todo_list, finished):
    return [todo_list[i] for i in range(len(finished)) if finished[i] == False]