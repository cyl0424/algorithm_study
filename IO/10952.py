# 0 0이 입력되기 전까지 두 정수 a, b의 합을 출력

while True :
  try :
    # 두 정수 a, b를 입력받음
    a, b = map(int, input().split())
    
    # a, b 모두 0이면 종료
    if (a == 0 and b == 0) :
      break
    
    # 그 외의 경우 a, b의 합을 출력
    else :
      print(a+b)
  
  except:
    break
