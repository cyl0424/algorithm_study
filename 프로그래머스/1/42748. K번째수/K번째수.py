def solution(array, commands):
    answer = []
    
    for c in commands:
        tmp = sorted(array[c[0]-1:c[1]])[c[2]-1]
        answer.append(tmp)
    return answer