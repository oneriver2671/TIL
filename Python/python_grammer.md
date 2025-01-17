
### 정수형/실수형

- 코테에서 이 정수형을 주로 다루게 됨.
- 실수형 : 4바이트, 8바이트 등 고정된 크기의 메모리를 할당하므로 컴퓨터 시스템은 실수 정보를 표현하는 정확도에 한계를 가짐. (ex - 10진수에서 0.3+0.6=0.9 이지만, 2진수는 정확히 표현할 방법이 없음. 미세한 오차 발생)
    
    ⇒ `round()` 함수를 이용하는 것이 권장됨. 주로 반올림해서 소수점 아래 몇째자리 까지의 정확성을 보장함.
    

### 지수 표현 방식
- 파이썬에선 e나 E를 이용해 지수 표현 방식을 사용할 수 있음.
- e나 E 다음에 오는 수는 10의 지수부를 의미함.
- 1e9 ⇒ 10의 9제곱
- '**최단 경로 알고리즘**'에서는 도달할 수 없는 노드에 대하여 최단 거리를 무한(INF)로 설정하곤 함.
⇒ 이때, 가능한 최댓값이 10억 미만이라면 무한(INF)의 값으로 1e9를 이용할 수 있음.

### 주로 사용하는 연산자
- 나누기 연산자(/) 사용 시 주의
    - 파이썬에선 나누기 연산자(/) 사용 시, **실수형으로 반환**됨.
- 나머지 연산자(%)
    - 사용 예시: a가 홀수인지 확인해야 하는 경우
- 몫 연산자(//)
- 거듭 제곱 연산자(**)

## 리스트 자료형

- 연결 리스트와 유사한 기능까지 지원함
- C++의 STL vector와 기능적으로 유사함 (Java는 ArrayList)
- 리스트 대신 배열 혹은 테이블이라 부르기도 한다.
- 거꾸로 인덱싱 가능 (음수 활용)
    
    ```python
    # 뒤에서 첫번째 원소 출력
    print(a[-1])
    ```
    
- **슬라이싱(Slicing)**
    - 연속적인 위치를 갖는 원소들을 가져와야 할 때 사용
    - 대괄호 안에 콜론(:)을 넣어서 **시작 인덱스**와 **끝 인덱스** 설정 가능
    - 참고: 끝 인덱스는 실제 인덱스보다 1을 더 크게 설정함
        
        ```python
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        # 두번째 ~ 네번째 원소 출력
        print(a[1 : 4])    # [1:3] 일 것 같은데 4까지 써줘야 함
        ```
        
- **리스트 컴프리헨션**
    - 리스트를 초기화하는 방법 중 하나. 대괄호 안에 조건문과 반복문을 적용해 리스트를 초기화 할 수 있다.
    
    ```python
    array = [i for i in range(10)]
    print(array)
    
    # 결과 : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ```
    
    ```python
    # 0 ~ 19까지의 수 중 홀수만 포함하는 리스트
    array = [i for i in range(20) if i % 2 == 1]
    
    # 1 ~ 9까지의 수들의 제곱 값을 포함하는 리스트
    array = [i * i for i in range(1, 10)]
    ```
    
    - **2차원 리스트**를 초기화할 때 효과적으로 사용할 수 있음. (N x M 크기)
        
        ```python
        # 좋은 예시
        array = [[0] * m for _in range(n)]
        
        # 잘못된 예시 (전체 리스트 안에 포함된 각 리스트가 모두 같은 객체로 인식되어버림)
        array = [[0] * m] * n
        ```
        
    

### 언더바 사용은 언제?

- 파이썬에선 반복을 수행할 때, 반복을 위한 변수의 값을 무시하고자 할 때 언더바(_)를 자주 씀.
(반복을 위해 사용한 변수가 사용되지 않을 때)
    
    ```python
    # "Hello World"를 5번 출력하기 (변수 불필요)
    for _ in range(5):
  	    print("Hello World")
    
    # 1~9까지의 자연수 더하기 (변수가 필요한 상황)
    sum = 0
    for i in range(1, 10):
        sum += i
    print(sum)
    ```
    

### 리스트 관련, 자주 사용하는 기타 메서드

![캡처075.png](imgs/캡처075.png)

- `remove()` : `removeAll()` 이 파이썬엔 없기 때문에, 특정한 값을 가진 원소를 모두 제거하기 위해선 별도의 로직이 필요함.
    
    ⇒ **집합** 자료형을 사용해야 함 (특정 원소의 존재 유무를 파악할 때 효과적으로 사용할 수 있음)
    
    ```python
    a = [1, 2, 3, 4, 5, 5, 5]
    remove_set = {3, 5}   # 집합 자료형
    
    #remove_list에 포함되지 않은 값만 저장
    result = [i for i in a if i not in remove_set]
    print(result)
    
    # 결과: [1, 2, 4]
    ```
    

## 문자열 자료형

- 다른 언어와 달리 큰 따옴표(”), 작은 따옴표(’) 모두 사용 가능
- 덧셈과 곱셈을 사용할 수 있음.
- 인덱싱과 슬라이싱 사용이 가능하나, 특정 인덱스의 값을 변경할 수는 없다.

## 튜플 자료형

- 리스트와 유사하나, 한 번 선언된 값을 변경할 수 없다.
⇒ 바뀌면 안되는 데이터를 저장하기 좋겠네.
- 소괄호(`()`)를 이용해 선언하되, 리스트처럼 `[]`로 특정 인덱스 값을 가져올 수 있음.
- 기능이 제한적이지만 리스트에 비해 상대적으로 **공간 효율적**이다. (더 적은 양의 메모리를 사용함)

```python
a = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# 두번째 ~ 네번째 원소 출력
print(a[1 : 4])
```

### 튜플을 사용하면 좋은 경우

- 서로 다른 성질의 데이터를 **묶어서 관리**해야 할 때
(회사에서 만든 NameValue<K,V> 와 비슷할 듯)
    - 최단 경로 알고리즘에서는 (비용, 노드 번호)의 형태로 튜플 자료형을 자주 사용함.
- 데이터의 나열을 해싱(Hasing)의 키 값으로 사용해야 할 때
    - 리스트와 다르게 변경이 불가능하니 키 값으로 사용 가능
- 리스트보다 메모리를 효율적으로 사용해야 할 때

## 사전 자료형


- 키(Key)와 값(Value)의 쌍을 데이터로 가지는 자료형으로, 다른 언어에선 해시 테이블로 불린다.
- 변경 불가능(Immutable) 자료형을 키로 사용할 수 있다.
- 사전 자료형은 해시 테이블(Hash Table)을 이용하므로, 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리할 수 있다.
- 키와 값을 별도로 뽑아내는 메서드를 제공한다.
    - `keys()` : 키 데이터만 뽑아서 리스트로 이용
    - `values()` : 값 데이터만 뽑아서 리스트로 이용

```python
# 사전 자료형 초기화1
a = dict()
a['key1'] = 1
a['key2'] = 2

# 사전 자료형 초기화2
b = {
	'key3': 3, 
	'key4': 4
}

key_list = list(b.keys())
```

## 집합 자료형


- 중복을 허용하지 않는다.
- 순서가 없다. (⇒ 인덱싱으로 값을 얻을 수 없음)
- 리스트 혹은 문자열을 이용해 초기화 할 수 있다. `set()` 함수 사용.
- 데이터의 조회 및 수정에 있어서 **O(1)**의 시간에 처리할 수 있다.

```python
# 집합 자료형 초기화 방법1
data = set([1, 1, 2, 3, 4, 4, 5])

# 집합 자료형 초기화 방법2
data = {1, 1, 2, 3, 4, 4, 5}
```

- 기본적으로 제공되는 집합 연산: 합집합, 교집합, 차집합

```python
# 합집합
print(a | b)

# 교집합
print(a & b)

# 차집합
print(a - b)
```

## 기본 입출력


### 자주 사용되는 표준 입력 방법 ★★

- `input()` 함수 : 한 줄의 문자열을 입력 받는 함수
- `map()` 함수 : 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용

```python
# 이렇게 써주면, 공백값 제거하면서 배열 만들어줌.
# 입력값 : 50 40 78 100
data = input().split()
print(data)

# 결과 : ['50', '40', '78', '100']

# 근데 정수형으로 바꾸고 싶음 -> map() 함수 활용 후 list() 감싸주기
data = list(map(int, input().split()))
print(data)

# 결과 : [50, 40, 78, 100]

# 데이터를 딱 3개만 입력받고 싶다?
a, b, c = map(int, input().split())
print(a, b, c)
```

⇒ 이거 많이 사용된다!! 손에 익을 정도로 많이 연습해둘 것 ★

### 빠르게 입력받는 법

- 파이썬의 sys 라이브러리에 있는 `sys.stdin.readline()` 메서드를 사용
    - 단, 입력 후 엔터(Enter)가 줄바꿈 기호로 입력되므로 `rstrip()` 메서드를 함께 사용

```python
import sys

# 문자열 입력 받기
data = sys.stdin.readline().rstrip()
print(data)
```

### 표준 출력 방법

- `print()` 함수 사용
- 기본적으로 출력 이후에 줄 바꿈을 수행하며, 줄 바꿈을 원치 않는 경우 `end` 속성을 이용할 수 있다.

```python
print(7, end=" ")
print(8, end=" ")

# 출력할 변수
answer = 7
print("정답은" + str(answer) + "입니다.")
```

- `str()` 함수 사용 이유
    - 파이썬은 문자열과 정수형을 직접적으로 더할 수 없어서, 정수형을 문자열로 변환.
- `f-string` 을 사용하면 `str()` 보다 더 간단하게 표현 가능
    - 문자열 앞에 접두사 ‘f’를 붙이면 됨. 파이썬 3.6부터 사용 가능.
    
    ```python
    answer = 7
    print(f"정답은 {answer}입니다.")
    
    # 결과
    # 정답은 7입니다.
    ```
    

## 조건문과 반복문


### 조건문

- 파이썬에선 **코드의 블록(Block)을 들여쓰기(Indent)로 지정**한다.
- `if` ~ `elif` ~ `else`
    - 보통 `else if`를 쓰는데 파이썬은 줄여서 `elif`
- 탭 vs 스페이스 여러번 사용? 두 진영이 나뉘어져 있음. 아직 활발히 논쟁 중.
- 파이썬 스타일 가이드라인 : 4개의 공백 문자로 들여쓰기 하는 것을 권장.

```python
score = 85

if score >= 70:
		print('성적이 70점 이상입니다.')
		if score >= 90:
				print('우수한 성적입니다.')
else:
		print('성적이 70점 미만입니다.')
		print('조금 더 분발하세요.')

print('프로그램을 종료합니다.')       # 이건 무조건 실행됨.

# 실행 결과
# 성적이 70점 이상입니다.
# 프로그램을 종료합니다.
```

- 간소화된 조건문 (if ~ else문을 한줄에 작성할 수 있음)
    
    ```python
    score = 85
    result = "Success" if score >= 80 else "Fail"
    
    print(result)
    ```
    

### 논리 연산자

- 다른 언어와 조금 차이가 있네. 좀 더 직관적이다.
- `X and Y` / `X or Y` / `not X`

```python
a = 15

if a >= 0 and a <= 20:
		print("a는 0 이상, 20 이하의 숫자입니다.")
```

### 기타 연산자

- `in`과 `not in` 연산자가 제공됨. (리스트, 튜플, 문자열, 딕셔너리 모두 사용 가능)
- `pass` : 아무것도 처리하고 싶지 않을 때 사용 가능
    
    ```python
    score = 85
    
    if score >= 80:
    		pass # 나중에 작성할 코드
    else:
    		print('성적이 80점 미만입니다.')
    ```


## 반복문

- while문, for문이 있는데 코테에선 for문이 더 간결한 경우가 많음.

```python
# while문 (1 ~ 9의 정수 중에서 홀수만 더하기)
i = 1
result = 0

while i <= 9:
	if i % 2 == 1:
		result += i
	i += 1

print(result)
```

```python
# for문
array = [1, 2, 3, 4, 5]

for x in array:
	print(x)
```

- 기본적인 for문이 c#에서 `foreach()`문과 유사하네. 배열에 있는 값을 하나씩 순서대로 가져오고 싶을 때 사용하면 되겠다.

### range(시작 값, 끝 값 + 1)

Java, C# 쪽에서 흔히 쓰던 `for(int i=0; i<=9; i++)` 문법을 쓰려면, 파이썬에선
`for(i in range(9))` ⇒ 이런식으로 내장 함수 `range()`를 써주면 됨.
(인자를 1개만 넣으면 자동으로 시작값은 0이 된다.)

```python
# i는 1~9까지의 모든 값을 순회
for i in range(1, 10)
	result += i

print(result)
```

### continue

반복문에서 남은 코드의 실행은 무시하고, 다음 반복을 진행하고자 할 때.

```python
# 1부터 9까지 홀수의 합 구하기
result = 0

for i in range(1, 10):
	if i % 2 == 0:
		continue
	result += i

print(result)
```

### break

```python
i = 1

while True:
	print("현재 i의 값:", i)
	if i == 5:
		break
	i += 1
```

# 함수와 람다 표현식

### global 키워드

변수에 `global` 키워드를 지정하면, 해당 함수에선 지역 변수를 만들지 않고 함수 바깥에 선언된 변수를 바로 참조하게 됨.

```python
a = 0

def func():
	global a    # 바깥의 변수 a를 참조한다.
	a += 1
```

- 참고: 전역변수로 선언된 리스트 객체의 내부 메서드를 수행하는 것은 오류없이 수행 가능하다.

```python
array = [1, 2, 3, 4, 5]

def func():
	array.append(6)
	print(array)

func()
```

### 여러 개의 반환값

- 파이썬에서의 함수는 여러개의 반환값을 가질 수 있다. (’**패킹**’이라고 함. 다시 담는 건 ‘언패킹’.)

```python
def operator(a, b):
	add_var = a + b
	subtract_var = a - b
	multiply_var = a * b
	divide_var = a / b
	return add_var, subtract_var, multiply_var, divide_var

a, b, c, d = operator(7, 3)
print(a, b, c, d)
```

### 람다 표현식

- 함수를 간단하게 작성할 수 있다. (이름없는 함수)
- 함수 자체를 입력으로 받는 함수에서 유용하게 사용 / 함수가 간단하거나 한번 쓰고 말 때

```python
def add(a, b):
	return a + b

#일반적인 add() 메서드 사용
print(add(3, 7))

# 람다 표현식으로 구현한 add() 메서드
print((lambda a, b: a + b)(3, 7))
```

```python
# 예시1: sort() 함수를 사용해 정렬할 때 유용하게 사용할 수 있다.

array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

# 람다 없이 함수 만들어 사용
def my_key(x):
    return x[1]

print(sorted(array, key=my_key))

# 람다 사용 시.
print(sorted(array, lambda x: x[1]))
```

예시2) 여러개의 리스트에 적용하기

```python
# 각 list별 같은 인덱스끼리 더하고 싶다.

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a + b, list1, list2)
print(list(result))

# 결과
# [7, 9, 11, 13, 15]
```

# 실전에서 유용한 표준 라이브러리

![2022-08-10 16 37 15.png](./imgs/2022-08-10_16_37_15.png)

### 자주 사용되는 내장 함수

- `sum()`, `min(), max()`, `eval()`
- `sorted()` : 각 원소를 정렬한 결과를 반환함.
    
    ```python
    # sorted()
    result = sorted([9, 1, 8, 5, 4])     # 오름차순
    reverse_result = sorted([9, 1, 8, 5, 4], reverse=True)     # 내림차순
    
    # sorted() with key : 정렬 기준을 명시할 수 있다.
    # 두번째 원소를 기준으로 내림차순 정렬하기
    array = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
    result = sorted(array, key=lambda x: x[1], reverse=True)
    ```
    

## 순열과 조합

- 순열은 순서 상관있음. ‘CAB’ ≠ ‘CBA’

![2022-08-10_16_51_23.png](./imgs/2022-08-10_16_51_23.png)

### 순열 라이브러리

```python
from itertools import permutations

data = ['A', 'B', 'C']

result = list(permutations(data, 3))     # 모든 순열 구하기 (3개를 골라 순서 나열)
print(result)
```

### 조합 라이브러리

```python
from itertools import combinations

data = ['A', 'B', 'C']

result = list(combinations(data, 2))
print(result)
```

### 중복 순열과 중복 조합

- `product` 라이브러리 - 중복 순열 구할 때
- `combinations_with_replacement` 라이브러리 - 중복 조합 구할 때

```python
from itertools from product

data = ['A', 'B', 'C']

# 2개를 뽑는 모든 순열 구하기 (중복 허용)
result = list(product(data, repeat=2)) 
print(result)

from itertools import combinations_with_replacement

data = ['A', 'B', 'C']

# 2개를 뽑는 모든 조합 구하기 (중복 허용)
result = list(combinations_with_replacement(data, 2))
print(result)
```

### Counter 라이브러리

- 파이썬 collections 라이브러리의 Counter는 등장 횟수를 세는 기능을 제공함.
- 리스트와 같은 반복 가능한 객체가 주어졌을 때, 내부의 원소가 각각 몇번씩 등장했는지 알려준다.

```python
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])     # 'blue'가 등장한 횟수 출력
print(counter['green'])    # 'green'이 등장한 횟수 출력
print(dict(counter))       # 사전 자료형으로 반환
```

### 최대 공약수와 최소 공배수

- `math` 라이브러리를 활용하면 된다. 최대공약수는 `gcd()`, 최소공배수는 직접 만들어줘야 함.

```python
import math

# 최소 공배수(LCM)을 구하는 함수
def lcm(a, b):
    return a * b // math.gcd(a, b)

a = 21
b = 14

print(math.gcd(21, 14))    # 최대 공약수(GCD) 계산
print(lcm(21, 14))         # 최소 공배수(LCM) 계산
```