num = int(input())

numList = list(map(int, input().split()))

numList.sort()

minNum = numList[0]
maxNum = numList[num-1]

print(f'{minNum} {maxNum}')