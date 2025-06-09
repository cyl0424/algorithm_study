def solution(s):
    answer = [0, 0]
    
    while s != "1":
        zero = s.count('0')
        answer[1] += zero
        
        s = s.replace('0', '')
        s = bin(len(s))[2:]
        
        answer[0] += 1
    return answer