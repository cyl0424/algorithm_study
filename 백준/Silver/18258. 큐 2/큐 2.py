import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
numbers = deque()

for _ in range(N):
    command = list(input().split())

    if command[0] == 'push':
        numbers.append(int(command[1]))
    elif command[0] == 'pop':
        if numbers:
            print(numbers.popleft())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(numbers))
    elif command[0] == 'empty':
        if numbers:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if numbers:
            print(numbers[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if numbers:
            print(numbers[-1])
        else:
            print(-1)
