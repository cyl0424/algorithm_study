def solution(food):
    answer = ''
    cnt = 1
    
    for f in food[1:]:
        if int(f)//2 >= 1:
            answer += str(cnt)*(int(f)//2)
        cnt += 1
    
    answer = answer + "0" + answer[::-1]
    return answer