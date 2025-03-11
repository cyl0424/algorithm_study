import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 해제

def dfs(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
        return 0  # 유효하지 않은 경우 0 반환

    grid[i][j] = '0'  # 방문 처리
    size = 1  # 현재 집 포함

    # 4방향 탐색하면서 집 개수 더하기
    size += dfs(grid, i + 1, j)
    size += dfs(grid, i - 1, j)
    size += dfs(grid, i, j + 1)
    size += dfs(grid, i, j - 1)

    return size

def numIslands(grid):
    num_of_house = []
    cnt = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':  # 새로운 단지 발견
                num_of_house.append(dfs(grid, i, j))
                cnt += 1  # 단지 개수 증가

    return cnt, num_of_house

# 입력 처리
N = int(input())
grid = [list(input().strip()) for _ in range(N)]  # 입력을 문자 그대로 유지 ('1', '0')

# 결과 출력
cnt, num_of_house = numIslands(grid)
print(cnt)
for num in sorted(num_of_house):
    print(num)
