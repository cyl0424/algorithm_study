def solution(s):
    if s.isdigit():
        return int(s)
    
    answer = s
    eng_num = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5',
              'six':'6', 'seven':'7', 'eight':'8', 'nine':'9', 'zero':'0'}
    
    for k in eng_num.keys():
        answer = answer.replace(k, eng_num[k])

    return int(answer)