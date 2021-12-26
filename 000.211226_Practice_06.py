# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 21:45:45 2021

@author: nnk
"""

# =============================================================================
# 문자열 처리 메서드
# =============================================================================
# 1. 기본 메서드 : 벡터 연산 불가 (각 원소마다 반복 불가)
'abc'.upper()                   # 'ABC'
'a/b/c'.split('/')              # ['a', 'b', 'c']
'a/b/c'.split('/')[1]           # 'b'

l1 = ['abc','def']
l2 = ['a/b/c','d/e/f']

# list는 안됨
l1.upper()
l2.split('/')

# list에서 각 원소를 돌리고 싶을 때, map
# map : list를 함수 처리 할 수 있음
list(map(lambda x: x.upper(),l1))
# ['ABC', 'DEF']
list(map(lambda x: x.split('/'), l2))
# [['a', 'b', 'c'], ['d', 'e', 'f']]
# list(map(lambda x: x.split('/')[1],'2') <- list가 아니라 안됨



# =============================================================================
# 2. pandas 메서드 : 벡터화 내장(매 원소마다 반복 가능)
# Series, DataFrame

# 1) split
from pandas import Series, DataFrame
s1 = Series(l1)
# 0    abc
# 1    def
# dtype: object
s2 = Series(l2)
# 0    a/b/c
# 1    d/e/f
# dtype: object

s2.str.split('/')
# 0    [a, b, c]
# 1    [d, e, f]
# dtype: object
# dtype이 object인 Series를 str으로 변환해주고 메서드를 사용

# 2) 대소 치환
s1.str.upper() # o
s1.str.lower() # o
s1.str.title() # o camel 형태
# 0    Abc
# 1    Def
# dtype: object

# 3) replace
s1.replace('a','A')                 # 변경 적용 안됨
# 0    abc
# 1    def
# dtype: object
s1.str.replace('a','A')             # replace 적용 됨
# 0    Abc
# 1    def
# dtype: object
s1.str.replace('a','')              # replace 중요 !**** 공백으로 만드는 것 ****
# 0     bc
# 1    def
# dtype: object


## 예제 : 숫자를 다 더한 정수로 나타내라
s3 = Series(['1,200','1,300','1,400'])
s3.sum() # '1,2001,3001,400'
#1
s3.str.replace(',','').astype('int').sum() # 3900
#2
s3 = s3.str.replace(',','')
sum(list(map(lambda x: int(x),s3))) # 3900

# 4) 패턴 확인
# startswith
# endswith
# contains
s1
# 0    abc
# 1    def
# dtype: object
s1.str.startswith('a')
# 0     True
# 1    False
# dtype: bool
s1[s1.str.startswith('a')]
# 0    abc
# dtype: object
s1[s1.str.endswith('c')]
# 0    abc
# dtype: object
s1[s1.str.contains('e')]
# 1    def
# dtype: object

# 문자열 크기
s1.str.len()
# 0    3
# 1    3
# dtype: int64

# 포함 개수
Series(['aabbbb','abcdadd']).str.contains('a')
# 0    True
# 1    True
# dtype: bool
Series(['aabbbb','abcdadd']).str.count('a')
# 0    2
# 1    2
# dtype: int64

# 공백,문자 제거 함수
Series(['      cd     ','        df       '])
# 0              cd     
# 1            df       
# dtype: object
Series(['      cd     ','        df       ']).str.strip()
# 0    cd
# 1    df
# dtype: object
Series(['      cd     ','        df       ']).str.strip().str.len() # 메소드체인
# 0    2
# 1    2
# dtype: int64

s1.str.strip('a')
# 0     bc
# 1    def
# dtype: object
Series(['aaabaaabcd','abcdaa']).str.strip('a') # 양 옆만 적용됨
# 0    baaabcd
# 1        bcd
# dtype: object
Series(['aaabaaabcd','abcdaa']).str.replace('a','') # 중간값도 삭제 가능
# 0    bbcd
# 1     bcd
# dtype: object

# find : 위치값
s5 = Series(['abc@naver.com','abcde@google.com'])
s5.str.find('@')
# 0    3
# 1    5
# dtype: int64

# 문자열 색인(추출)
'abcde'[0:3] # 'abc'
s5[0:3]
# 0       abc@naver.com
# 1    abcde@google.com
# dtype: object
s5.str[0:3]
# 0    abc
# 1    abc
# dtype: object

## 예제 : 이메일 아이디 추출
vno = s5.str.find('@')
list(map(lambda x, y: x[0:y],s5,vno))
# ['abc', 'abcde']
s5.map(lambda x: x[:x.find('@')])
# 0      abc
# 1    abcde
# dtype: object

# pad : 문자열 삽입
# s1.str.pad(5,        # 총 자리수
#            'left',   # 삽입 방향
#            '!')     # 삽입 글자

s1
# 0    abc
# 1    def
dtype: object
s1.str.pad(5,'left','!')
# 0    !!abc
# 1    !!def
# dtype: object
s1.str.pad(5,'right','^')
# 0    abc^^
# 1    def^^
# dtype: object
s6 = Series(["I love you","You know"])
s6.str.pad(20, 'right', '^')
# 0    I love you^^^^^^^^^^
# 1    You know^^^^^^^^^^^^
# dtype: object

# 문자열 결합
s7 = Series(['abc', 'def', '123'])
s7.str.cat()                # 'abcdef123'
s7.str.cat(sep=',')         # 'abc,def,123'
s7.str.cat(sep='/')         # 'abc/def/123'

s8 = Series([['a','b','c'], ['d','e','f']])
s8.str.join(sep='')
# 0    abc
# 1    def
# dtype: object
s8.str.join(sep=',')
# 0    a,b,c
# 1    d,e,f
# dtype: object

# Series 는
Series(['a','b','c'],index = ['11','22','33'])
Series(['a','b','c'],['11','22','33'])




