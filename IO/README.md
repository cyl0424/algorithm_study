## Solved
- [2557](https://github.com/cyl0424/baeckjoon_python/blob/main/IO/2557.py), [1000](https://github.com/cyl0424/baeckjoon_python/blob/main/IO/1000.py), [2558](https://github.com/cyl0424/baeckjoon_python/blob/main/IO/2558.py), [10950](https://github.com/cyl0424/baeckjoon_python/blob/main/IO/10950.py), [10951](https://github.com/cyl0424/baeckjoon_python/blob/main/IO/10951.py), [10952](https://github.com/cyl0424/baeckjoon_python/blob/main/IO/10952.py), [10953](https://github.com/cyl0424/baeckjoon_python/blob/main/IO/10953.py), [11021](https://github.com/cyl0424/baeckjoon_python/blob/main/IO/11021.py), [11022](https://github.com/cyl0424/baeckjoon_python/blob/main/IO/11022.py), [11718](https://github.com/cyl0424/baeckjoon_python/blob/main/IO/11718.py), [11719](https://github.com/cyl0424/baeckjoon_python/blob/main/IO/11719.py), [11720](https://github.com/cyl0424/baeckjoon_python/blob/main/IO/11720.py), [11721](https://github.com/cyl0424/baeckjoon_python/blob/main/IO/11721.py)
    
<br>

## Note
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
