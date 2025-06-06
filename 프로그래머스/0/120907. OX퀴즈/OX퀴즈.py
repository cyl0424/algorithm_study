def solution(quiz):
    answer = []
    xo = ["X", "O"]
    for q in quiz:
        new_q = q.split(" ")
        
        if new_q[1] == '-':
            answer.append(xo[int(int(new_q[0]) - int(new_q[2]) == int(new_q[-1]))])
        else:
            answer.append(xo[int(int(new_q[0]) + int(new_q[2]) == int(new_q[-1]))])
    return answer