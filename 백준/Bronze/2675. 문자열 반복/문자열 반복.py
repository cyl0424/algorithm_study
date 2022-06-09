num = int(input())

for _ in range(num) :
    n, word = input().split()
    for i in word:
        print(i*int(n), end="")
    print()