def solution(n):
    answer = 0
    
    prefix = [0] * (n+1)
    
    for i in range(1, n+1):
        prefix[i] = prefix[i-1] + i
    
    start, end = 0, 1
    
    while start < end <= n:
        tmp = prefix[end] - prefix[start]
        
        if tmp < n:
            end += 1
        elif tmp > n:
            start += 1
        else:
            answer += 1
            end += 1
            
    return answer