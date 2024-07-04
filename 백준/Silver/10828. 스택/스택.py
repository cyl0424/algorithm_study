import sys
input = sys.stdin.readline

def stPush(st:list, x):
    st.append(x)

def stPop(st:list):
    try:
        print(st.pop())
    except:
        print(-1)

def stTop(st:list):
    if len(st) > 0:
        print(st[len(st)-1])
    else:
        print(-1)

def stSize(st:list):
    print(len(st))

def stEmpty(st:list):
    if len(st) == 0:
        print(1)
    else:
        print(0)


def stack(st, inst):
    if('push' in inst):
        _, n = inst.split()
        stPush(st, int(n))

    elif(inst == 'pop'):
        stPop(st)

    elif(inst == 'top'):
        stTop(st)
    
    elif(inst == 'empty'):
        stEmpty(st)
    
    elif(inst == 'size'):
        stSize(st)
    
stk = []
N = int(input())

for _ in range(N):
    inst = str(input()).strip()
    stack(stk, inst)