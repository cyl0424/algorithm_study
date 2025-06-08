def solution(dartResult):
    score = [0]
    
    tmp = ''
    
    for d in dartResult:
        if d.isdigit():
            tmp += d
        elif tmp != '':
            score.append(int(tmp))
            tmp = ''
            
            if d == 'D':
                idx = len(score) - 1
                score[idx] **= 2
            elif d == 'T':
                idx = len(score) - 1
                score[idx] **= 3
        else:
            if d == '*':
                idx = len(score) - 1
                score[idx] *= 2
                score[idx - 1] *= 2
            elif d == '#':
                idx = len(score) - 1
                score[idx] *= -1
                
    return sum(score)