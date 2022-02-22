# 입력받은 값을 그대로 출력 (입력값이 없으면 중단)

while True :
  # 정상적으로 입력될 경우 입력값 출력
  try :
    print(input())
  
  # 입력값이 없으면 중단
  except EOFError :
    break
