def solution(n):
    answer = n+1
    
    n_one = bin(n)[2:].count('1')
    
    while bin(answer)[2:].count('1') != n_one:
        answer += 1
        
    return answer