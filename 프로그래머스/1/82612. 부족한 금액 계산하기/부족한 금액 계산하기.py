def solution(price, money, count):
    answer = -1
    
    total = price * (count*(count+1)//2)
    answer = total - money
    
    if answer <= 0:
        return 0
    
    return answer