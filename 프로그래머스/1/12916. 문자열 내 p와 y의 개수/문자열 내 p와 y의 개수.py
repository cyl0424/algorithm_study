def solution(s):
    answer = True
    
    s = s.lower()
    answer = s.count('p') == s.count('y')

    return answer