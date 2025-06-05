from collections import Counter

def solution(array):
    if len(array) == 1:
        return array[0]
    
    counter = Counter(array)
    commons = counter.most_common(2)
    
    if len(commons) == 1 or commons[0][1] != commons[1][1]:
        return commons[0][0]
    
    return -1