n = int(input())

if n == 1:
    print(0)

else:
    for i in range(1, n):
        new_i = list(str(i))
        if i + sum(map(int, new_i)) == n:
            print(i)
            break

        elif i == n-1:
            print(0)