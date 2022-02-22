# 입력된 테스트 케이스 횟수만큼 콤마로 구문된 두 정수 a, b의 합을 구해 출력

# 테스트 케이스 횟수를 입력받아 num에 저장
num = int(input())

# 입력받은 횟수만큼 a, b를 입력받아 합을 출력
for i in range(num):
  try:
    a, b = map(int, input().split(','))
    print(a+b)

  except:
    break
