def solution(s):
    answer = []
    passed = ''
    
    for i in range(len(s)):
        if s[i] not in passed:
            answer.append(-1)
        else:
            answer.append(i-passed.rfind(s[i]))
            
        passed += s[i]
    return answer