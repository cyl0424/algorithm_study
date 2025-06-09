def solution(n):
    answer = 0
    a, b = 0, 1
    
    for i in range(2, n+1):
        tmp = (a + b) % 1234567
        a, b = b, tmp
    
    return b