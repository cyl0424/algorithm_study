def solution(s, n):
    answer = ''
    tmp = []
    
    for l in list(s):
        if l == " ":
            tmp.append(" ")
            
        else:
            new = (ord(l)+n)
        
            if new > ord('z') and l.islower():
                new -= 26

            elif new > ord('Z') and l.isupper():
                new -= 26

            tmp.append(chr(new))
        
    answer = ''.join(tmp)
    return answer