import sys
input = sys.stdin.readline

n = int(input()) # 도시의 수
distances = list(map(int, input().split())) # 도시 간 거리
prices = list(map(int, input().split())) # 도시별 기름 가격

answer = 0
start = True
min_price = prices[0]

for i, d in enumerate(distances):
    if prices[i] >= min_price:
        answer += min_price * d
    else:
        answer += prices[i] * d
        min_price = prices[i]

print(answer)