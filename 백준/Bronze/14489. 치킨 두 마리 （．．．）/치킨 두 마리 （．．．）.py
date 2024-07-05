a1, a2 = map(int, input().split())
ch = int(input())

if a1+a2 >= ch*2:
    print(a1+a2-ch*2)
else:
    print(a1+a2)