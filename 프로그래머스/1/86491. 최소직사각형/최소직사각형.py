def solution(sizes):
    answer = 0
    x = []
    y = []
    
    for s in sizes:
        x.append(min(s))
        y.append(max(s))
        
    answer = max(x) * max(y)
    return answer