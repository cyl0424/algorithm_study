# 입력받은 케이스 테스트 횟수만큼 두 정수 a, b의 값 더해 출력

num = int(input()) # 케이스 테스트 횟수를 입력받아 num에 저장

for i in range(num):
  a, b = map(int, input().split())
  
  print(a+b)
