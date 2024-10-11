from collections import Counter

def solution(clothes):
    answer = 1
    
    key_counts = Counter(key for _, key in clothes)
    key_counts_dict = dict(key_counts)
    
    cnt_list = key_counts_dict.values()
    
    for i in cnt_list:
        answer *= i + 1
        
    answer -= 1
    
    return answer