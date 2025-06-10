import math

def solution(n, words):
    answer = []
    
    word = words[0]
    repeat = [word]

    for idx, w in enumerate(words[1:], start = 2):
        if word[-1] != w[0] or w in repeat:
            word = w
            
            num = idx % n if idx % n != 0 else n
            cnt = math.ceil(idx / n)
            
            answer = [num, cnt]
            
            break
        
        repeat.append(w)
        word = w
        
        if w == words[-1]:
            answer = [0, 0]
            
    return answer
