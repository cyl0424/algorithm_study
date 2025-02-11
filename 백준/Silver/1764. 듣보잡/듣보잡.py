import sys

input = sys.stdin.readline

n, m = map(int, input().split())
answer = []

never_listen = set(input().strip() for _ in range(n))

for _ in range(m):
    never_see = input().strip()
    if never_see in never_listen:
        answer.append(never_see)

answer.sort()

print(len(answer))

for a in answer:
    print(a)