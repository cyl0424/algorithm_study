def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        if cnt_num(i) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer

def cnt_num(n):
    cnt = 1 if int(n**0.5) == n**0.5 else 0
    for i in range(1, int(n**0.5)):
        cnt += 2
    return cnt