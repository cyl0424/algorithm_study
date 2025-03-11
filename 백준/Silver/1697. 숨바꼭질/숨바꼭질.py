import sys
from collections import deque

input = sys.stdin.readline

MAX = 100001
N, K = map(int, input().split())
'''
N: 수빈이가 있는 위치
K: 동생이 있는 위치
'''

def bfs(start):
    queue = deque([start])
    visited = [0] * MAX

    while queue:
        current = queue.popleft()
        if current == K:
            return visited[current]
        for next in (current - 1, current + 1, current * 2):
            if 0 <= next < MAX and visited[next] == 0:
                visited[next] = visited[current] + 1
                queue.append(next)

print(bfs(N))