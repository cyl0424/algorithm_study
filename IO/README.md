# Solved
- 2557, 1000

# Note
- map(함수, 리스트 or 튜플) : 리스트 or 튜플의 요소를 지정된 함수로 처리해주는 함수

	
	example code
	```
	a, b = map(int, input().split())
	```
	description
	```
	# split()을 이용해 input으로 받은 값을 리스트로 저장
	numList = input().split()
	
	# numList의 요소를 map()을 이용해 int로 변환
	numInt = map(int, numList)
	
	# numInt의 int 값을 변수 a, b에 저장
	a, b = numInt
	```
	###### 참고 : [파이썬 코딩도장: 22.6 리스트에 map 사용하기](https://dojang.io/mod/page/view.php?id=2286)
