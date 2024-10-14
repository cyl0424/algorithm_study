from itertools import combinations

def solution(numbers):
    answer = []
    
    cases = list(combinations(numbers, 2))
    
    for c in cases:
        res = sum(c)
        if res not in answer:
            answer.append(res)
    
    answer.sort()
    return answer