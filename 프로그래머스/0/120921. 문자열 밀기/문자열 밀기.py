from collections import deque

def solution(A, B):
    A = deque(A)
    B = deque(B)
    
    cnt = 0
    
    for i in range(len(A)):
        if A == B:
            break
            
        A.rotate(1)
        cnt += 1
    
        if i == len(A)-1:
            cnt = -1

    return cnt