from collections import Counter

def solution(clothes):
    key_counts = Counter(key for _, key in clothes)
    print(key_counts)
    
    answer = 1
    for count in key_counts.values():
        answer *= count + 1
    
    return answer - 1