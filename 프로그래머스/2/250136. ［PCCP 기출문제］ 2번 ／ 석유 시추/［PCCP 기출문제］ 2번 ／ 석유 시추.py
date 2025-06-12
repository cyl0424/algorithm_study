def solution(land):
    # land[row][col]
    row_len, col_len = len(land), len(land[0])
    oils = [0] * col_len
    
    dc = [1, -1, 0, 0]
    dr = [0, 0, 1, -1]
    
    def dfs(r, c):
        stack = [(r, c)]
        land[r][c] = 0
        oil_cells = []
        
        while stack:
            nr, nc = stack.pop()
            oil_cells.append((nr, nc))
            
            for dir in range(4):
                tr, tc = nr + dr[dir], nc + dc[dir]
                
                if 0 <= tr < row_len and 0 <= tc < col_len and land[tr][tc] == 1:
                    stack.append((tr, tc))
                    land[tr][tc] = 0
                
        return oil_cells
    
    for col in range(col_len):
        for row in range(row_len):
            if land[row][col] == 1:
                oil_cells = dfs(row, col)
                
                oil_cols = set()
                for cell in oil_cells:
                    oil_cols.add(cell[1])
                
                oil_volume = len(oil_cells)
                for oil_col in oil_cols:
                    oils[oil_col] += oil_volume
    
    return max(oils)
    