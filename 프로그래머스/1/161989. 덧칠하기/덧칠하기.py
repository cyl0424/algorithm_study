def solution(n, m, section):
    answer = 0
    prev = 0
    
    for s in section:
        if prev == 0:
            prev = s
            answer += 1
        elif prev + m - 1 >= s:
            pass
        else:
            answer += 1
            prev = s
    return answer