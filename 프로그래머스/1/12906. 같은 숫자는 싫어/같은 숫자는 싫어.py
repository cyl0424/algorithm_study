from collections import Counter

def solution(arr):
    answer = [arr[0]]
    
    tmp = arr[0]
    for i in range(1, len(arr)):
        if tmp != arr[i]:
            answer.append(arr[i])
        tmp = arr[i]
        
    return answer