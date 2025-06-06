def solution(code):
    mode = 0
    code = list(code)
    answer = ''
    
    for i in range(len(code)):
        c = code[i]
        
        if c == '1':
            mode = (mode + 1) % 2
        elif mode == 0 and i % 2 == 0:
            answer += c
        elif mode == 1 and i % 2 == 1:
            answer += c
            
    return answer if len(answer) > 0 else "EMPTY"