import sys
from collections import Counter

input = sys.stdin.readline

V = int(input())
vote = Counter(input().strip())

A = vote['A']
B = vote['B']

if A > B:
    print('A')
elif A < B:
    print('B')
else:
    print('Tie')