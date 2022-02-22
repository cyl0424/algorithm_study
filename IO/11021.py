# 입력받은 테스트 케이스 횟수만큼 두 정수 a, b의 합을 'Case #n : 00'의 형식으로 출력

# 테스트 케이스 횟수를 num에 저장
num = int(input())

for i in range (num):
  try :
    a, b = map(int, input().split())
    print(f'Case #{i+1}: {a+b}')
  
  except :
    break
