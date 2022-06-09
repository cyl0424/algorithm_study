while True :
  # a, b를 입력받으면 합을 출력
  try :
    a, b = map(int, input().split())
    
    print(a+b)
  
  # 입력 값이 없을 경우 중단
  except EOFError:
    break