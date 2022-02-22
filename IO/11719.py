# 입력받은 값을 그대로 출력 (공백이 있으면 공백 그대로 출력)

while True :
  try :
    print(input())
  
  except EOFError :
    break
