# Python Coding Test Cheat Sheet

## Table of Contents
1. [Built-in Functions](#built-in-functions)
   - [Math Functions](#math-functions)
   - [Type Conversion](#type-conversion)
   - [Iterables and Iteration](#iterables-and-iteration)
2. [Standard Libraries](#standard-libraries)
   - [Collections](#collections)
   - [Heapq](#heapq)
   - [Itertools](#itertools)
   - [Functools](#functools)
3. [String Manipulation](#string-manipulation)
4. [Example Problems](#example-problems)

## Built-in Functions

### Math Functions

#### `abs()`
숫자의 절대값을 반환합니다.

```python
print(abs(-5))  # 출력: 5
```

#### `min()`, `max()`
이터러블에서 가장 작은 값과 가장 큰 값을 반환하거나, 두 개 이상의 인자 중에서 가장 작은 값과 큰 값을 반환합니다.

```python
print(min(3, 1, 4, 1, 5))  # 출력: 1
print(max(3, 1, 4, 1, 5))  # 출력: 5
```

#### `sum()`
이터러블의 모든 요소를 합산합니다.

```python
print(sum([1, 2, 3, 4, 5]))  # 출력: 15
```

#### `pow()`
거듭제곱을 반환합니다.

```python
print(pow(2, 3))  # 출력: 8
```

### Type Conversion

#### `int()`, `float()`
숫자나 문자열을 정수나 부동 소수점 숫자로 변환합니다.

```python
print(int("10"))  # 출력: 10
print(float("10.5"))  # 출력: 10.5
```

#### `str()`
객체를 문자열로 변환합니다.

```python
print(str(10))  # 출력: '10'
```

#### `list()`, `tuple()`, `set()`
이터러블을 리스트, 튜플, 세트로 변환합니다.

```python
print(list("abc"))  # 출력: ['a', 'b', 'c']
print(tuple([1, 2, 3]))  # 출력: (1, 2, 3)
print(set([1, 2, 2, 3]))  # 출력: {1, 2, 3}
```

### Iterables and Iteration

#### `len()`
객체의 길이를 반환합니다.

```python
print(len("hello"))  # 출력: 5
```

#### `enumerate()`
이터러블의 모든 항목에 대해 인덱스와 값을 쌍으로 가지는 열거 객체를 반환합니다.

```python
for index, value in enumerate(["a", "b", "c"]):
    print(index, value)
# 출력:
# 0 a
# 1 b
# 2 c
```

#### `zip()`
각 이터러블에서 동일한 인덱스에 있는 요소들을 튜플로 묶어서 반환하는 이터레이터를 반환합니다.

```python
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for item in zip(list1, list2):
    print(item)
# 출력:
# (1, 'a')
# (2, 'b')
# (3, 'c')
```

#### `filter()`
조건을 만족하는 요소들로 이루어진 이터레이터를 반환합니다.

```python
nums = [1, 2, 3, 4, 5]
even_nums = filter(lambda x: x % 2 == 0, nums)
print(list(even_nums))  # 출력: [2, 4]
```

#### `map()`
모든 요소에 함수를 적용한 결과를 반환합니다.

```python
nums = [1, 2, 3, 4, 5]
squared_nums = map(lambda x: x**2, nums)
print(list(squared_nums))  # 출력: [1, 4, 9, 16, 25]
```

#### `sorted()`
정렬된 리스트를 반환합니다.

```python
nums = [3, 1, 4, 1, 5, 9]
print(sorted(nums))  # 출력: [1, 1, 3, 4, 5, 9]
```

## Standard Libraries

### Collections

#### `Counter`
해시 가능한 객체를 세는 딕셔너리의 하위 클래스입니다.

```python
from collections import Counter

counter = Counter([1, 2, 2, 3, 3, 3])
print(counter)  # 출력: Counter({3: 3, 2: 2, 1: 1})
```

#### `deque`
양쪽 끝에서 빠른 추가 및 제거가 가능한 리스트와 같은 컨테이너입니다.

```python
from collections import deque

dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print(dq)  # 출력: deque([0, 1, 2, 3, 4])
```

#### `defaultdict`
기본 값을 제공하는 딕셔너리의 하위 클래스입니다.

```python
from collections import defaultdict

dd = defaultdict(int)
dd['a'] += 1
print(dd)  # 출력: defaultdict(<class 'int'>, {'a': 1})
```

#### `OrderedDict`
순서를 유지하는 딕셔너리의 하위 클래스입니다.

```python
from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
print(od)  # 출력: OrderedDict([('a', 1), ('b', 2)])
```

### Heapq

#### `heapq.heappush()`, `heapq.heappop()`
힙 큐 알고리즘(우선순위 큐)입니다.

```python
import heapq

heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
print(heapq.heappop(heap))  # 출력: 1
```

### Itertools

#### `itertools.permutations()`
이터러블의 요소들로 구성된 r-길이의 순열을 반환합니다.

```python
from itertools import permutations

perm = permutations([1, 2, 3])
for p in perm:
    print(p)
# 출력:
# (1, 2, 3)
# (1, 3, 2)
# (2, 1, 3)
# (2, 3, 1)
# (3, 1, 2)
# (3, 2, 1)
```

#### `itertools.combinations()`
이터러블의 요소들로 구성된 r-길이의 조합을 반환합니다.

```python
from itertools import combinations

comb = combinations([1, 2, 3], 2)
for c in comb:
    print(c)
# 출력:
# (1, 2)
# (1, 3)
# (2, 3)
```

#### `itertools.product()`
모든 가능한 (카르테시안) 곱을 반환합니다.

```python
from itertools import product

prod = product([1, 2], ['a', 'b'])
for p in prod:
    print(p)
# 출력:
# (1, 'a')
# (1, 'b')
# (2, 'a')
# (2, 'b')
```

### Functools

#### `functools.lru_cache()`
메모이제이션을 위해 최대 maxsize만큼의 최근 호출 결과를 저장하는 데코레이터입니다.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # 출력: 55
```

#### `functools.reduce()`
함수를 누적 적용하여 이터러블을 단일 값으로 줄입니다.

```python
from functools import reduce

nums = [1, 2, 3, 4, 5]
sum_nums = reduce(lambda x, y: x + y, nums)
print(sum_nums)  # 출력: 15
```

## String Manipulation

### `split()`, `join()`
문자열을 리스트로 분리하거나 리스트를 문자열로 결합합니다.

```python
s = "hello world"
print(s.split())  # 출력: ['hello', 'world']

words = ['hello', 'world']
print(' '.join(words))  # 출력: 'hello world'
```

### `replace()`
문자열 내의 일부 문자열을 다른 문자열로 대체합니다.

```python
s = "hello world"
print(s.replace("world", "there"))  # 출력: 'hello there'
```

### `strip()`
문자열의 앞

뒤 공백을 제거합니다.

```python
s = "  hello world  "
print(s.strip())  # 출력: 'hello world'
```

### `startswith()`, `endswith()`
문자열이 특정 접두사나 접미사로 시작하거나 끝나는지 여부를 확인합니다.

```python
s = "hello world"
print(s.startswith("hello"))  # 출력: True
print(s.endswith("world"))    # 출력: True
```

### `find()`, `rfind()`
문자열 내에서 부분 문자열을 찾고, 해당 부분 문자열이 처음이나 마지막으로 발견된 인덱스를 반환합니다.

```python
s = "hello world"
print(s.find("o"))  # 출력: 4
print(s.rfind("o")) # 출력: 7
```

## Example Problems

### Problem 1: Two Sum

#### Description
정수 배열 `nums`와 정수 `target`이 주어졌을 때, 합이 `target`이 되는 두 숫자의 인덱스를 반환합니다.

#### Solution

```python
def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

print(two_sum([2, 7, 11, 15], 9))  # 출력: [0, 1]
```

### Problem 2: Reverse a String

#### Description
문자열을 뒤집는 함수를 작성하세요.

#### Solution

```python
def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))  # 출력: 'olleh'
```
