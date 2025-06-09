import math

def solution(brown, yellow):
    answer = []
    h, w = 0, 0
    
    for i in range(1, math.ceil(math.sqrt(yellow)) + 1):
        if yellow % i == 0:
            h = i + 2
            w = yellow // i + 2
            
            total = 2 * (h + w) - 4

            if total == brown:
                answer = [w, h]
                break
            
    return answer