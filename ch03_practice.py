# 3-1 연산자
print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2**3)
print(5%3)
print(10//3)

print(10 > 3)
print(4 >= 7)

print(1 != 3)
print(not(1 != 3))

print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 5))

print((3 > 0) and (3 < 5))
print((3 > 0) | (3 < 5))

# 3-2 간단한 수식
number = 2 + 3 + 5
print(number)
number += 2
print(number)

# 3-3 숫자 처리 함수
print(abs(-5))
print(pow(4,2))
print(max(5,12))
print(min(5,12))
print(round(3.14))
print(round(4.99))

from math import *
print(floor(4.99))
print(ceil(3.14))
print(sqrt(16))

# 3-4 랜덤 함수
from random import *
print(random())
print(int(random() * 10))

print(randrange(1, 46))
print(randint(1,45))
