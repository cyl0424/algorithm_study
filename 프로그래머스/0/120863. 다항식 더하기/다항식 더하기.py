def solution(polynomial):
    answer = []
    
    polynomial = polynomial.split(" + ")
    
    x = 0
    c = 0
    
    for p in polynomial:
        if 'x' in p:
            p = p.replace('x', '')
            x += 1 if p == '' else int(p)
        else:
            c += int(p)
    
    if x:
        if x == 1:
            answer.append("x")
        else:
            answer.append(f"{x}x")
    
    if c:
        answer.append(str(c))
        
    return ' + '.join(answer)