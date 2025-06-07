def solution(babbling):
    answer = 0
    available = ["aya", "ye", "woo", "ma"]
    
    for b in babbling:
        for a in available:
            if a*2 not in b:
                b = b.replace(a, ' ')
                
            if b.isspace():
                answer += 1
                break
    
    return answer