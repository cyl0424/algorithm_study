import sys
input = sys.stdin.readline

# 테스트에 사용한 내비게이션의 수
N = int(input())

# 시작점과 도착점의 좌표
s_x, s_y, e_x, e_y = map(int, input().split())
navi_res = []

for _ in range(N):
    # 순차적으로 방문해야하는 중간 지점의 개수
    M = int(input())
    distance = 0

    x, y = s_x, s_y

    for i in range(M+1):
        if i != M:
            nx, ny = map(int, input().split())
            distance += abs(x-nx) + abs(y-ny)
            x, y = nx, ny
        else:
            distance += abs(x-e_x) + abs(y-e_y)
     
    navi_res.append(distance)

print(navi_res.index(min(navi_res))+1)
