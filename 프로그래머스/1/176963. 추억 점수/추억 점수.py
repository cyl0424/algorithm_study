def solution(name, yearning, photo):
    answer = []
    scores = dict(zip(name, yearning))
    
    for p in photo:
        total = 0
        for n in p:
            if n in name:
                total += scores[n]
        answer.append(total)
    return answer