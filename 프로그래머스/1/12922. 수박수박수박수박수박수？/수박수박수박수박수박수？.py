import math

def solution(n):
    answer = '수박' * math.ceil(n/2)
    answer = answer[:n]
    return answer