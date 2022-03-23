# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 22:05:26 2021

@author: nnk
"""
# =============================================================================
# pandas 문자열메서드
# =============================================================================
'abc'.upper()
'a/b/c'.split('/')

# 기본 메서드 : 벡터 연산 불가 (매 원소마다 반복 안됨)
l1 = ['abc','def']
l2 = ['a/b/c','d/e/f']
l1.upper()      # AttributeError: 'list' object has no attribute 'upper'
l2.upper()      # AttributeError: 'list' object has no attribute 'upper'


# map
list(map(lambda x: x.upper(),l1))           # ['ABC', 'DEF']
list(map(lambda x: x.split('/'),l2))        # [['a', 'b', 'c'], ['d', 'e', 'f']]



# =============================================================================
# pandas 메서드 : 벡터화 내장 (매 원소마다 반복 가능)
# Series, DataFrame

from pandas import Series, DataFrame
s1 = Series(l1)
'''
0    abc
1    def
dtype: object
'''
s2 = Series(l2)
'''
0    a/b/c
1    d/e/f
dtype: object
'''

# 1) split
s2.split('/') # AttributeError: 'Series' object has no attribute 'split'
s2.str.split('/')
'''
0    [a, b, c]
1    [d, e, f]
dtype: object
'''
# 대소치환
s1.str.upper()
'''
0    ABC
1    DEF
dtype: object
'''
s1.str.lower()
'''
0    abc
1    def
dtype: object
'''
s1.str.title()
'''
0    Abc
1    Def
dtype: object
'''


# 2) replace 치환
s1.str.replace('a','A')
'''
0    Abc
1    def
dtype: object
'''
s1.str.replace('a','')
'''
0     bc
1    def
dtype: object
'''


# 예제) 천단위 구분기호 처리
s3 = Series(['1,200','3,000','4,000'])
'''
0    1,200
1    3,000
2    4,000
dtype: object
'''
s3.sum() # '1,2003,0004,000'

s3.str.replace(',','').astype('int').sum() # 8200

# 패턴 확인 : startswith, endswith, contains
s1.str.startswith('a')
'''
0     True
1    False
dtype: bool
'''
s1[s1.str.startswith('a')] # s1 각 원소에서 a로 시작하는 원소 추출
'''
0    abc
dtype: object
'''
s1[s1.str.endswith('c')] # s1 각 원소에서 c로 끝나는 원소 추출
'''
0    abc
dtype: object
'''
s1[s1.str.contains('e')] # s1 각 원소에서 e를 포함하는 원소 추출
'''
1    def
dtype: object
'''


# 문자열 크기 : len
s1.str.len()
'''
0    3
1    3
dtype: int64
'''
# count
Series(['aabca','abcdsa']).str.count('a')
'''
0    3
1    2
dtype: int64
'''
# 문자열 제거 : strip
# 공백
Series(['       cd  ','    df  ']).str.strip()
'''
0    cd
1    df
dtype: object
'''
Series(['       cd  ','    df  ']).str.strip().str.len()
'''
0    2
1    2
dtype: int64
'''
# 문자
Series(['aaaabaca','abcaa']).str.strip('a') # 중간값 제거안됨
'''
0    bac
1     bc
dtype: object
'''
Series(['aaaabaca','abcaa']).str.replace('a','') # 중간값 제거 가능
'''
0    bc
1    bc
dtype: object
'''

# find
s4 = Series(['abc@abc.com','avcvdds@abc.com'])
s4.str.find('@')
'''
0    3
1    7
dtype: int64
'''

# 문자열 색인(추출)
'abcded'[0:3] # 'abc'
s4.str[0:3]
'''
0    abc
1    avc
dtype: object
'''

# 예제) 이메일 아이디 추출
vno = s4.str.find('@')
list(map(lambda x,y: x[0:y], s4,vno)) # ['abc', 'avcvdds']

list(s4.map(lambda x: x[0:x.find('@')]))

# pad : 문자열 삽입
s1.str.pad(5, 'left', '!')
'''
0    !!abc
1    !!def
dtype: object
'''
s1.str.pad(5, 'right', '^')
'''
0    abc^^
1    def^^
dtype: object
'''

# cat : 문자열 결합
s5 = Series(['abc','def','123'])
s5.str.cat() # 'abcdef123'
s5.str.cat(sep='/') # 'abc/def/123'

s6  = Series([['a','b','c'],['d','e','f']])
'''
0    [a, b, c]
1    [d, e, f]
dtype: object
'''

s6.str.join(sep='')
'''
0    abc
1    def
dtype: object
'''
s6.str.join(sep=',')
'''
0    a,b,c
1    d,e,f
dtype: object
'''