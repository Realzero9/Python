# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 13:13:35 2021

@author: nnk
"""

# =============================================================================
# 사용자 정의 함수
# 사용자가 정의하는 함수의 형태
# input과 output 관계를 내부에 정의
# def, lambda(축약형)
# =============================================================================

# 함수  : f(x) = x + 1

# =============================================================================
 # def 함수이름(인수1, 인수2, 인수3):
 #     함수식
 #     return 반환할 객체
# =============================================================================

def f_mul(x):
    re = x * 10
    return re
f_mul(5) # 50

def f_mul2(x, y):
    return x*y
f_mul2(2,10) # 20

# =============================================================================
# 인수에 default 값 넣어줄 수 있음
def f_d(x=1,y=1):
    return x*y
f_d()

def f_d1(y,x=1):
    return x*y
f_d1(5)

# default 값은 먼저 정의 할 수 없음
# def f_d2(x=1, y):
#     return x*y
# f_d2(5) # SyntaxError: non-default argument follows default argument
# =============================================================================




# =============================================================================
# lambda 축약형 (한줄코드)
# 비교적 단순한 연산 및 리턴시 사용
# =============================================================================

la1 = lambda x: x*10
la1(5) # 50

la2 = lambda x,y,z: (x+y)*z
la2(2,3,4) # 20

# =============================================================================
# map 함수 - 리스트를 함수처리 할 수 있음
# =============================================================================

m1 = lambda x: x*3
l1 = [1,2,5,10]
m1(l1) # [1, 2, 5, 10, 1, 2, 5, 10, 1, 2, 5, 10] 리스트의 반복



# =============================================================================
# 1. for 문
l2 =[]
for i in l1:
    l2.append(i+10)
print(l2)
# [11, 12, 15, 20]

# =============================================================================
# 2. def + map
# map(func,     # 함수                  ex) x+1
#     iterable) # 반복가능한 추가할 인수 ex) [1,2,3,4]
# =============================================================================

m1 = lambda x: x*3
list(map(m1, l1))
# [3, 6, 15, 30]

l3 = [3,5,7,10]
def cal(x):
    if x>10:
        re = x*3
    else:
        re = x*2
    return re
cal(11) # 33
cal(5) # 10
cal(l3)
# TypeError: '>' not supported between instances of 'list' and 'int'

list(map(cal,l3))
# [6, 10, 14, 20]