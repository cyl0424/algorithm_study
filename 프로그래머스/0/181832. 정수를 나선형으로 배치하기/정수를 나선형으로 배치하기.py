def solution(n):
    answer = [[0] * n for _ in range(n)]
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    
    idx = 0
    
    x = 0
    y = 0
    
    for i in range(n*n):
        answer[y][x] = i + 1
        
        nx = x + dx[idx]
        ny = y + dy[idx]
        
        if nx < 0 or nx >= n or ny < 0 or ny >= n or answer[ny][nx] != 0:
            idx = (idx + 1) % 4
            x += dx[idx]
            y += dy[idx]
        else:
            x = nx
            y = ny
        
    return answer