import math, sys
input = sys.stdin.readline

N = int(input())
tList = list(map(int, input().split()))
T, P = map(int, input().split())

t = 0

for i in tList:
    t += math.ceil(i/T)

print(t)

pSet = N // P
pNum = N - pSet*P

print(pSet, pNum)