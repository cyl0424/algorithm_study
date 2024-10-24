def solution(d, budget):
    answer = 0
    spend = 0
    
    d.sort()
    
    for money in d:
        spend += money
        
        if spend > budget:
            break
        else:
            answer += 1
            
    return answer