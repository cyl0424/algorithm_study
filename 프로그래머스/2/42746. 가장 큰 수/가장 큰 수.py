def solution(numbers):
    numbers = sorted(numbers, key = lambda x: str(x)*3, reverse=True)
    answer = ''.join(map(str, numbers))
    
    return str(int(answer)) # 00일 경우 0으로 출력되도록 하기 위해 str -> int -> str로 출력