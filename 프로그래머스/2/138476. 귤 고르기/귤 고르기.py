from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    tangerine = Counter(tangerine)
    tangerine = sorted(tangerine.items(), key = lambda pair: pair[1])
    
    while k > 0:
        k -= tangerine.pop()[1]
        answer += 1
    
    return answer