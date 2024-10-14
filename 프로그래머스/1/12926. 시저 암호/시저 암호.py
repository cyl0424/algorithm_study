def solution(s, n):
    answer = []
    
    for l in s:
        if l == " ":
            answer.append(" ")
        else:
            new = ord(l) + n
            if l.islower() and new > ord('z'):
                new -= 26
            elif l.isupper() and new > ord('Z'):
                new -= 26
            answer.append(chr(new))
    
    return ''.join(answer)
