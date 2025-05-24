T = int(input())
answer = [0] * 11

for i in range(1, 11):
    if i % 2 == 0:
        answer[i] = answer[i-1] - i
    else:
        answer[i] = answer[i - 1] + i

for test_case in range(1, T+1):
    N = int(input())

    print(f"#{test_case} {answer[N]}")