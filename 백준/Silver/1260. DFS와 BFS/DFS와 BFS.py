from collections import defaultdict, deque

n, m, v = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 양방향 그래프 처리

# 정점 번호 작은 순서대로 방문하도록 정렬
for key in graph:
    graph[key].sort()

def bfs(start_v, graph):
    visited = set()
    queue = deque([start_v])
    result = []

    while queue:
        vertex = queue.popleft()
        if vertex in visited:
            continue

        visited.add(vertex)
        result.append(vertex)

        for w in graph[vertex]:
            if w not in visited:  # 이미 방문한 정점은 추가하지 않음
                queue.append(w)

    return result


def dfs(start_v, graph):
    visited = []
    
    def recursive_dfs(v):
        visited.append(v)
        for w in graph[v]:
            if w not in visited:
                recursive_dfs(w)
    
    recursive_dfs(start_v)
    return visited

print(*dfs(v, graph))
print(*bfs(v, graph))
