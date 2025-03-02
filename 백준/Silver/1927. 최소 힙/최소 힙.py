import sys
from heapq import heappush, heappop
import heapq

input = sys.stdin.readline

heap = []

N = int(input())

for i in range(N):
    number = int(input())
    
    if number == 0:
        if len(heap) == 0:
            print("0")
        else:
            print(heappop(heap))
    else:
        heappush(heap, number)