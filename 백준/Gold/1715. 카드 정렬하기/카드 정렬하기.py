import heapq
import sys
input = sys.stdin.readline

size = []
res = 0

for _ in range(int(input())):
    heapq.heappush(size, int(input()))

while len(size) > 1:
    new_size = heapq.heappop(size) + heapq.heappop(size)
    res += new_size
    heapq.heappush(size, new_size)

print(res)
