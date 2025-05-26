import sys
from collections import deque

input = sys.stdin.readline
dq = deque()
output = []

for _ in range(int(input())):
    cmd = input().split()
    c = cmd[0][0]

    if c == 'p':  # push or pop
        if cmd[0][1] == 'u':  # push
            dq.append(cmd[1])
        else:  # pop
            output.append(dq.popleft() if dq else '-1')
    elif c == 's':  # size
        output.append(str(len(dq)))
    elif c == 'e':  # empty
        output.append('0' if dq else '1')
    elif c == 'f':  # front
        output.append(dq[0] if dq else '-1')
    else:        # back
        output.append(dq[-1] if dq else '-1')

sys.stdout.write('\n'.join(output))