from collections import Counter

def solution(participant, completion):
    answer = ''
    
    participant_dict = dict(Counter(participant))
    
    for c in completion:
        participant_dict[c] -= 1
        if participant_dict[c] <= 0:
            del participant_dict[c]
    
    answer = list(participant_dict.keys())[0]
            
    return answer