import sys
input = sys.stdin.readline

T = int(input())

for i in range(1, T+1):
    print(f"Material Management {i}")
    N = int(input())
    A, B = map(int, input().split())

    for _ in range(N):
        u, v = map(int, input().split())
    print("Classification ---- End!")
