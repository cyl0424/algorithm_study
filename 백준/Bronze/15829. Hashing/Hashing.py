n = int(input())
alph = list(input().lower())
all = 0

for i in range(n):
    all += (ord(alph[i])-96) * pow(31,i)

print(all%1234567891)