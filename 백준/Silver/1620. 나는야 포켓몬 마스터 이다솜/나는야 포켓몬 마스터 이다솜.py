import sys

input = sys.stdin.readline

N, M = map(int, input().split())
poketmon = {}

for i in range(1, N + 1):
    poketmon[input().strip()] = i

poketmon_list = list(poketmon.keys())

for _ in range(M):
    quiz = input().strip()
    answer = ''

    if quiz.isdigit():
        answer = poketmon_list[int(quiz) - 1]
    else:
        answer = poketmon[quiz]

    print(answer)