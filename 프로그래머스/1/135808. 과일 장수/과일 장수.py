def solution(k, m, score):
    answer = 0
    cnt = len(score)//m
    score.sort(reverse=True)
    
    for i in range(cnt):
        answer += min(score[i*m:(1+i)*m]) * m
    return answer