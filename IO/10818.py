# N개의 숫자 중 최솟값, 최댓값 출력

num = int(input())

# list()를 이용해 입력받은 숫자들을 numList에 리스트 형태로 저장
numList = list(map(int, input().split())
               
# sort()를 이용해 numList의 요소를 오름차순으로 정렬
numList.sort()

# 최솟값인 인덱스 0의 요소와, 최댓값인 인덱스 -1의 요소를 순서대로 출력
print(numList[0], numList[-1])
