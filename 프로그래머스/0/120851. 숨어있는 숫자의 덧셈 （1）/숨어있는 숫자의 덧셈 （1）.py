def solution(my_string):
    answer = []
    
    for s in list(my_string):
        if s.isdigit():
            answer.append(int(s))
    
    return sum(answer)