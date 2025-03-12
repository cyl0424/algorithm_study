import sys

input = sys.stdin.readline
S = set()
all_nums = set(range(1, 21))

m = int(input().strip())

for _ in range(m):
    cmd = input().strip().split()
    
    if cmd[0] == "all":
        S = all_nums.copy()
    elif cmd[0] == "empty":
        S.clear()
    else:
        num = int(cmd[1])
        if cmd[0] == "add":
            S.add(num)
        elif cmd[0] == "remove":
            S.discard(num)
        elif cmd[0] == "check":
            print(1 if num in S else 0)
        elif cmd[0] == "toggle":
            S ^= {num}  # XOR 연산을 이용한 toggle