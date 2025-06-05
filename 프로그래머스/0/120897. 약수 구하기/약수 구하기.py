import math

def solution(n):
    answer = set()
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            answer.add(i)
            answer.add(n // i)
        
    answer = sorted(list(answer))
    return answer