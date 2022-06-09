import sys
import heapq as hq

n = int(sys.stdin.readline())
numbers = []

for _ in range(n):
    new_n = int(sys.stdin.readline())

    if new_n == 0:
        print(hq.heappop(numbers)[1] if numbers else 0)
    else:
        hq.heappush(numbers, (abs(new_n), new_n))