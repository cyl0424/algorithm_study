def solution(numbers):
    numbers = sorted(numbers, key=lambda x: str(x)*3, reverse=True)
    
    answer = ''.join(map(str, numbers))
    
    return str(int(answer))