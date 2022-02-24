# N개의 숫자 중 최솟값, 최댓값 출력

num = int(input())

numList = list(map(int, input().split()))

numList.sort()

print(numList[0], numList[-1])
