## Notes
- **map(함수, 리스트 or 튜플) :** 리스트 or 튜플의 요소를 지정된 함수로 처리해주는 함수   
	
	***example code***
	```
	a, b = map(int, input().split())
	```
	***description***
	```
	# split()을 이용해 input으로 받은 값을 리스트로 저장
	numList = input().split()
	
	# numList의 요소를 map()을 이용해 int로 변환
	numInt = map(int, numList)
	
	# numInt의 int 값을 변수 a, b에 저장
	a, b = numInt
	```
	###### 참고 : [파이썬 코딩도장: 22.6 리스트에 map 사용하기](https://dojang.io/mod/page/view.php?id=2286)

<br>

- **EOFError 예외처리 :** 입력값이 없는 예외를 처리하기 위해 사용   

	***example code***
	```
	while True : 
	  try : 
	    print(input())
	  
	  except EOFError : 
	    break
	``` 
	***description***
	```
	1. 입력이 끝날때까지 input 값을 출력
	2. 입력이 끝나면 while 문이 break되어 중단
	```

<br>

- **sort(reverse = True/False) :** 리스트의 값을 정렬하기 위해 사용(False가 기본값)   

	***example code***
	```
	numList = [1, 3, 2, 4, 6, 5]
	
	numList.sort()
	print(numList)
	
	numList.sort(reverse = True)
	print(numList)
	``` 
	***description***
	```
	# sort()를 사용할 경우 리스트의 요소를 오름차순으로 정렬
	numList.sort()
	
	# 출력 값은 [1, 2, 3, 4, 5, 6]
	print(numList)
	
	# sort(reverse = True)를 사용할 경우 리스트의 요소를 내림차순으로 정렬
	numList.sort(reverse = True)
	
	# 출력 값은 [6, 5, 4, 3, 2, 1]
	print(numList)
	```
	
	###### 참고 : [파이썬 - 기본을 갈고 닦자! 15. List(리스트)(5) - 리스트 정렬](https://wikidocs.net/16041)
