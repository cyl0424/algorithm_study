def solution(x):
    s = sum(int(digit) for digit in str(x))
    answer = x % s == 0
    return answer