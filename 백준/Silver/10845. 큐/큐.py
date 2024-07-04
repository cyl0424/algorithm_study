import sys
input = sys.stdin.readline

def quPush(qu:list, x):
    qu.insert(0, x)

def quPop(qu:list):
    try:
        print(qu.pop())
    except:
        print(-1)

def quFront(qu:list):
    if len(qu) > 0:
        print(qu[len(qu)-1])
    else:
        print(-1)

def quBack(qu:list):
    if len(qu) > 0:
        print(qu[0])
    else:
        print(-1)

def quSize(qu:list):
    print(len(qu))

def quEmpty(qu:list):
    if len(qu) == 0:
        print(1)
    else:
        print(0)


def queue(qu, inst):
    if('push' in inst):
        _, n = inst.split()
        quPush(qu, int(n))

    elif(inst == 'pop'):
        quPop(qu)

    elif(inst == 'front'):
        quFront(qu)

    elif(inst == 'back'):
        quBack(qu)

    elif(inst == 'size'):
        quSize(qu)

    elif(inst == 'empty'):
        quEmpty(qu)
    
que = []
N = int(input())

for _ in range(N):
    inst = str(input()).strip()
    queue(que, inst)