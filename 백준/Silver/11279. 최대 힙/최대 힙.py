import sys
from heapq import heappop, heappush
import heapq

input = sys.stdin.readline

N = int(input())

heap = []

for i in range(N):
    number = int(input())
    
    if number == 0:
        if len(heap) == 0:
            print("0")
        else:
            print(heappop(heap)[1])
    else:
        # heapq는 최소힙이므로, 최대합 구현을 위해 튜플을 사용함
        heappush(heap, (-number, number))