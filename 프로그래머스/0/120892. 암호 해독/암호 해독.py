def solution(cipher, code):
    cipher = list(cipher)
    answer = ''
    
    for i in range(code-1, len(cipher), code):
        answer += cipher[i]
    
    return answer