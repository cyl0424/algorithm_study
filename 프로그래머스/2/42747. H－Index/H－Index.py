def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    
    for i, v in enumerate(citations, start = 1):
        if v >= i:
            answer = i
        
    return answer