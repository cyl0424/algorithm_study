def solution(board):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, 1, -1, -1, 0, 1]
    bombs = []
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                bombs.append([i, j])
    
    for bomb in bombs:
        for i in range(len(dx)):
            nx = bomb[0] + dx[i]
            ny = bomb[1] + dy[i]
            n = len(board)
            
            if 0 <= nx < n and 0 <= ny < n:
                board[nx][ny] = 1
    
    answer = 0
                    
    for i in range(len(board)):
        answer += board[i].count(0)
    
    return answer
        