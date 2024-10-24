import math

def solution(n, m):
    gcd = math.gcd(n, m)
    answer = [gcd, (n * m) / gcd]
    return answer