n = int(input())
files = []

if n == 1:
    print(input())

else:
    for _ in range(n):
        files.append(input())

    result = ['']*len(files[0])

    for j in range(len(files[0])):
        for i in range(1, n):
            if files[0][j] == files[i][j]:
                result[j] = files[0][j]
            else:
                result[j] = '?'
                break

    print(''.join(result))
