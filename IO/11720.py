# 입력받은 N개의 숫자를 합하여 출력

# 입력받을 숫자의 갯수를 num에 저장
num = int(input())

# 합할 num개의 수를 문자열(리스트)로 저장
numList = input()

# 결과값 sum을 초기화
sum = 0

# num과 numList의 길이가 일치할 경우에만 동작하도록 조건문 작성
if len(numList) == num :
  for i in range(num) :
    # numList의 요소를 int로 변환하여 더하기
    sum += int(numList[i])
  
  # numList의 모든 요소를 더한 값 sum을 출력
  print(sum)
