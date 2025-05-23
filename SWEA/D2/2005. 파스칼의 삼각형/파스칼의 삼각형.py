T = int(input())

for test_case in range(1, T + 1):
    num = int(input())
    triangle = []

    print(f"#{test_case}")
    for i in range(num):
        tmp = []
        for j in range(i+1):
            if j == 0 or j == i:
                tmp.append(1)
            else:
                tmp.append(triangle[i-1][j-1] + triangle[i-1][j])

        triangle.append(tmp)
        print(*tmp)