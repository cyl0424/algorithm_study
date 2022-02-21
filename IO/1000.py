# 두 정수를 입력받은 후, 합을 출력

# map 함수의 input().split()를 이용해 입력받은 값을 리스트로 저장
# 리스트 요소를 int로 변환한 후 언패킹을 통해 변수 a, b에 각각 저장
a, b = map(int, input().split())

# int a, b의 값을 더한 후 출력
print(a+b)
