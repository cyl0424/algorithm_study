def solution(hp):
    answer = 0
    
    if hp >= 5:
        ants = hp // 5
        answer += ants
        hp -= 5 * ants
        
    if hp >= 3:
        ants = hp // 3
        answer += ants
        hp -= 3 * ants
        
    if hp > 0:
        answer += hp
    
    return answer
    