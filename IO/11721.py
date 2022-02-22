# 입력받은 문자열을 10개씩 잘라 출력 (마지막이 10개가 안될 경우에는 10개 미만 글자만 출력)

# 입력받은 문자열을 strInput에 저장
strInput = input()

# i가 strInput 길이 내에서 10씩 커지도록 range의 step을 10으로 설정
for i in range(0, len(strInput), 10):
  # strInput에서 10개씩 끊어 출력
  print(strInput[i:i+10])
