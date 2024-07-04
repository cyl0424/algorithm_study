from itertools import combinations

# 첫 번째 줄 입력

N, M = map(int, input().split())

# 두 번째 줄 입력

cards = list(map(int, input().split()))

# 최대 합을 저장할 변수 초기화

max_sum = 0

# 모든 가능한 3장 카드 조합을 탐색

for combo in combinations(cards, 3):

    current_sum = sum(combo)

    if current_sum <= M and current_sum > max_sum:

        max_sum = current_sum

# 결과 출력

print(max_sum)