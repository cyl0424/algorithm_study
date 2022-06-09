num = int(input())
intList = []

for i in range(num):
    inputNum = int(input())
    intList.append(inputNum)

intList.sort()

for j in intList:
    print(j)