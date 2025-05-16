import heapq
import sys
input = sys.stdin.readline

n = int(input())

sizes = list(map(int, (input() for _ in range(n))))
heapq.heapify(sizes)

res = 0

while len(sizes) > 1:
    new_size = heapq.heappop(sizes) + heapq.heappop(sizes)
    res += new_size
    heapq.heappush(sizes, new_size)

print(res)