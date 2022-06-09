n = int(input())
temp = n

cnt = 0

a = temp // 10
b = temp % 10

while 10 * a + b != n or cnt == 0:
    temp = b * 10 + (a + b) % 10
    a = temp // 10
    b = temp % 10

    cnt += 1

print(cnt)