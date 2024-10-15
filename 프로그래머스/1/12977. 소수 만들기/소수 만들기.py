from itertools import combinations as comb

def solution(nums):
    answer = 0
    cases = list(sum(c) for c in comb(nums, 3))
    
    for c in cases:
        is_prime = True
        
        if c**0.5 == int(c**0.5):
            pass
        else:
            for i in range(2, int(c**0.5)+1):
                if c % i == 0:
                    is_prime = False
                    break
            if is_prime:
                answer += 1
    return answer