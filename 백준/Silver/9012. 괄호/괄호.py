n = int(input())

for _ in range(n):
    test = []
    ex = input()
    isVPS = "YES"
    for i in ex:
        if i == '(':
            test.append(i)
        elif i == ')':
            if len(test) == 0:
                isVPS="NO"
            else:
                test.pop()
    if test:
        isVPS = "NO"

    print(isVPS)