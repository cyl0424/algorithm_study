def solution(s):
    s = s.lower()
    s = s.split(" ")
    
    for i in range(len(s)):
        s[i] = s[i].capitalize()
    
    return ' '.join(s)