def solution(k, score):
    answer = []
    
    for i in range(len(score)):
        if i < k:
            answer.append(min(score[:i+1]))
        else:
            answer.append(sorted(score[:i+1], reverse = True)[k-1])
    return answer