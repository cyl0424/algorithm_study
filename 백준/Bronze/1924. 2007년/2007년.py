d_num = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ('MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN')

m, d = map(int, input().split())
diff = 0

if m != 1:
    for i in range(m-1):
        diff += d_num[i]

diff += d -1


print(days[diff % 7])

