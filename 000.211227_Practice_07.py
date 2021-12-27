# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 21:05:39 2021

@author: nnk
"""

# =============================================================================
# 07. Pandas _ Series, DataFrame
# 기본 암기 코드
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
# =============================================================================
# pandas : 2차원 정형 데이터
# =============================================================================
# 1. Series : 기본, 1차원, 하나의 데이터타입만 가능
s1 = Series([1, 2, 3, 4])
# 0    1
# 1    2
# 2    3
# 3    4
# dtype: int64
s2 = Series([1, 2, 3, '4'])
# 0    1
# 1    2
# 2    3
# 3    4
# dtype: object                 # str으로 인식하여 object
s3 = Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
# a    1
# b    2
# c    3
# d    4
# dtype: int64
s4 = Series(s3, index=['A', 'B', 'C', 'D'])
# A   NaN
# B   NaN
# C   NaN
# D   NaN
# dtype: float64                # 이미 idx가 존재하여 새로운 Series화

# 색인(indexing)
s1
# 0    1
# 1    2
# 2    3
# 3    4
# dtype: int64
s1[0]  # 1                       # 차원 축소 일어남 >> scalar 값
s1[0:1]                         # 차원 축소 없음   >> Series 값
# 0    1
# dtype: int64
s1[[0, 3]]                       # 차원 축소 없음   >> Series 값
# 0    1
# 3    4
# dtype: int64

s3
# a    1
# b    2
# c    3
# d    4
# dtype: int64
s3['a']  # 1
s3[['a', 'c']]
# a    1
# c    3
# dtype: int64
s3['a':'c']                     # 인덱스 슬라이싱은 마지막 범위 포함 됨
# a    1
# b    2
# c    3
# dtype: int64

s1 > 2
# 0    False
# 1    False
# 2     True
# 3     True
# dtype: bool
s1[s1 > 2]
# 2    3
# 3    4
# dtype: int64
s3
# a    1
# b    2
# c    3
# d    4
# dtype: int64
s3.b  # 2                        # key indexing (.index)
# index 문자로 지정했을 경우만 key indexing이 가능하고 기본index는 메서드호출 불가
# Series에서는 key indexing은 왼쪽 행인덱스 호출가능하고,
# DataFrame(2차원)에서는 위쪽 열인덱스 호출가능


# =============================================================================
#  연산
s1 + 1
# 0    2
# 1    3
# 2    4
# 3    5
# dtype: int64
s5 = Series([10, 20, 30, 40])
s6 = Series([10, 20, 30, 40], index=['c', 'd', 'e', 'f'])
s1+s5
# 0    11
# 1    22
# 2    33
# 3    44
# dtype: int64
s3 + s6
# a     NaN
# b     NaN
# c    13.0
# d    24.0
# e     NaN
# f     NaN
# dtype: float64
# index가 같은 경우만 같은 값끼리 연산가능, 다르면 NaN으로 출력

# =============================================================================
s3.add(s6, fill_value=0)
# a     1.0
# b     2.0
# c    13.0
# d    24.0
# e    30.0
# f    40.0
# dtype: float64
# s3에 s6을 add하는데 빈자리는 fill_value입력 값으로 채워줌
# Na 출력 방지용: 양쪽 모두 존재하고있지 않은 index는 Na값 발생!

s3.sub(s6, fill_value=0)  # 뺄셈
# a     1.0
# b     2.0
# c    -7.0
# d   -16.0
# e   -30.0
# f   -40.0
# dtype: float64
s3.mul(s6, fill_value=1)  # 곱셈
# a     1.0
# b     2.0
# c    30.0
# d    80.0
# e    30.0
# f    40.0
# dtype: float64
s3.div(s6, fill_value=1)  # 나눗셈
# a    1.000000
# b    2.000000
# c    0.300000
# d    0.200000
# e    0.033333
# f    0.025000
# dtype: float64

# iloc : 인덱스 열

# =============================================================================
# Series 기본 메서드
# 1. 데이터타입, 2. 인덱스, 3. 값 확인하기
s1.dtype  # dtype('int64') 데이터 타입 출력
s1.index  # RangeIndex(start=0, stop=4, step=1) 인덱스 출력
s3.index  # Index(['a', 'b', 'c', 'd'], dtype='object') 인덱스 출력
s3.values  # array([1, 2, 3, 4], dtype=int64) 값 (Value) 출력

s3[['c', 'd', 'a', 'b']]               # index 순서 변경 (색인)
# c    3
# d    4
# a    1
# b    2
# dtype: int64
s3.reindex(['c', 'd', 'a', 'b'])       # index 순서 변경 (메서드)
# c    3
# d    4
# a    1
# b    2
# dtype: int64
s3.index = ['A', 'B', 'C', 'D']        # index 수정
# A    1
# B    2
# C    3
# D    4
# dtype: int64
s3[0] = 10                          # 해당 index의 값 수정
# A    10
# B     2
# C     3
# D     4
# dtype: int64


# =============================================================================
# 2. DataFrame : 2차원 (행, 열)
# 생성
df1 = {'name': ['smith', 'will'], 'sal': [900, 1800]}
# {'name': ['smith', 'will'], 'sal': [900, 1800]}
df2 = DataFrame(df1)
#     name   sal
# 0  smith   900
# 1   will  1800

import numpy as np

df3 = DataFrame(np.arange(1,7).reshape(2,3), 
                index = ['a','b'], columns=['col1','col2','col3'])
#    col1  col2  col3
# a     1     2     3
# b     4     5     6
df3.col1                        # DataFrame에서의 key indexing
# a    1
# b    4
# Name: col1, dtype: int32
df3.a                           # 행인덱스 호출 불가
# AttributeError: 'DataFrame' object has no attribute 'a'
df3['col1']
# a    1
# b    4
# Name: col1, dtype: int32

# =============================================================================
# iloc, loc ***중요***
# iloc : positional indexing * 위치 ; 딥러닝
# loc : label indexing * 레이블
# =============================================================================
df3.iloc[:,0]                           # 열인덱스 위치값으로 가져오기
# a    1
# b    4
# Name: col1, dtype: int32
df3.iloc[:,0:3]
#    col1  col2  col3
# a     1     2     3
# b     4     5     6
df3.iloc[:,[0,-1]]
#    col1  col3
# a     1     3
# b     4     6

df3.loc[:,['col1','col3']]              # 컬럼명으로 가져오기
#    col1  col3
# a     1     3
# b     4     6


# 조건 색인 처리
df3.loc[df3.col1 == 1,:]
#    col1  col2  col3
# a     1     2     3

# =============================================================================
# DataFrame 기본 메서드
df3.dtypes # 각 컬럼 별 데이터 타입 확인 (type's' !!)
# col1    int32
# col2    int32
# col3    int32
# dtype: object
df3.index
# Index(['a', 'b'], dtype='object')
df3.columns
# Index(['col1', 'col2', 'col3'], dtype='object')
df3.values
# array([[1, 2, 3],
#        [4, 5, 6]])

df3
#    col1  col2  col3
# a     1     2     3
# b     4     5     6
df3.columns = ['A','B','C']         # 컬럼명 변경
#    A  B  C
# a  1  2  3
# b  4  5  6


# =============================================================================
# 연산
df3 + 10                        # 각 값에 덧셈 가능
#     A   B   C
# a  11  12  13
# b  14  15  16

df4 = DataFrame({'A':[10,40], 'B':[20,30], 'C':[30,80]}, index = ['a','b'])
#     A   B   C
# a  10  20  30
# b  40  30  80
df5 = DataFrame({'A':[10,40], 'B':[20,30]}, index = ['a','b'])
#     A   B
# a  10  20
# b  40  30

df3 + df5
#     A   B   C
# a  11  22 NaN
# b  44  35 NaN

# NaN 값 없애기
df3.add(df5, fill_value=0)
#     A   B    C
# a  11  22  3.0
# b  44  35  6.0