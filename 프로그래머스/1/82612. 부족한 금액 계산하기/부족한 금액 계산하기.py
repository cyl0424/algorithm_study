def solution(price, money, count):
    answer = -1
    
    total = price * sum(range(1, count+1))
    answer = total - money
    
    if answer <= 0:
        return 0
    
    return answer