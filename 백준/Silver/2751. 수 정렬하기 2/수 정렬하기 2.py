import sys

num = int(input())
intList = []

for i in range(num):
    inputNum = int(sys.stdin.readline())
    intList.append(inputNum)

intList.sort()

for j in intList:
    print(j)