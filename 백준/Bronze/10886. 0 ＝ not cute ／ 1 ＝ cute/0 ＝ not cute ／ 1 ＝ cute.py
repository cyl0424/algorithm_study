import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

zero = 0
one = 0

for _ in range(N):
    vote = int(input())

    if vote == 0:
        zero += 1
    else:
        one += 1

if one > zero:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')