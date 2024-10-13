def solution(a, b):
    answer = 0
    
    new_a = min(a, b)
    new_b = max(a, b)
    
    for i in range(new_a, new_b+1):
        answer += i
    return answer