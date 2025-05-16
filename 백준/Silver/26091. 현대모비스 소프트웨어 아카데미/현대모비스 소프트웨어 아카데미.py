import sys
input = sys.stdin.readline

N, M = map(int, input().split())
members = sorted(list(map(int, input().split())))

left, right = 0, N-1
answer = 0

while left < right:
    tmp = members[left] + members[right]
    if tmp >= M:
        answer += 1
        right -= 1
        left += 1
    else:
        left += 1

print(answer)