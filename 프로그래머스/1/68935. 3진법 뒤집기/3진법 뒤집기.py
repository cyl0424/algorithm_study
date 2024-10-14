def solution(n):
    answer = 0
    tmp = ''
    
    while n > 0:
        tmp += str(n % 3)
        n //= 3
    
    answer = int(tmp, 3)
        
    return answer