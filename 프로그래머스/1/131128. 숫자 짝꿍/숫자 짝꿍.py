def solution(X, Y):
    answer = ''
    cnt_x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    cnt_y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    for x in X:
        cnt_x[int(x)] += 1
    
    for y in Y:
        cnt_y[int(y)] += 1
    
    for i in range(9, -1, -1):
        answer += str(i) * min(cnt_x[i], cnt_y[i])
    
    if len(answer) == 0:
        return '-1'
    elif answer[0] == '0':
        return '0'
    else:
        return answer