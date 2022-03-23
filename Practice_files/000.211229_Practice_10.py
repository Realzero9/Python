# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 20:03:15 2021

@author: nnk
"""

# replace : 치환, 삭제

# =============================================================================
# 1. 기본 문자열 메서드
# - 기본 파이선 제공
# - 문자열에서 호출 가능
# - 벡터 연산(각 원소별 반복처리)불가
# - 오직 문자열 치환만 가능(숫자치환, Na 치환 불가능)
# =============================================================================

'abcd'.replace('a','A')         # 'Abcd'
'abcd'.replace('a','')          # 'bcd'
'abcd1'.replace(1,'') # TypeError: replace() argument 1 must be str, not int
' bcd1'.replace(' ',1) # TypeError: replace() argument 2 must be str, not int
['abcd','abcde','aabb'].replace(',','')
# AttributeError: 'list' object has no attribute 'replace'


# 1. for문 활용
outlist = []
for i in ['abcd','abcde','aabb']:
    outlist.append(i.replace('a','A'))
print(outlist) # ['Abcd', 'Abcde', 'AAbb']

# 2. map함수
f1 = lambda x: x.replace('a','A')
list(map(f1,['abcd','abcde','aabb']))
# ['Abcd', 'Abcde', 'AAbb']

['abcd','abcde','aabb'].map(f1)
# AttributeError: 'list' object has no attribute 'map'
# list는 map 호출 불가

from pandas import Series, DataFrame
# Series는 map 호출 가능
s1 = Series(['abcd','abcde','aabb']).map(f1)
'''
0     Abcd
1    Abcde
2     AAbb
dtype: object
'''

import numpy as np
s2 = Series(['abcd','abcde','aabb', np.nan])
'''
0     abcd
1    abcde
2     aabb
3      NaN
dtype: object
'''
s2.map(lambda x: x.replace(np.nan, ''))
# TypeError: replace() argument 1 must be str, not float / str 문자열만 가능

# =============================================================================
# 2.str.replace
# - pandas 제공 (Series 객체만 호출 가능)
# - 벡터화 내장된 문자열 메서드
# - 문자열 호출 가능
# - 벡터 연산(각 원소별 반복 처리) 가능
# - 오직 문자열 치환만 가능(숫자 치환, NA 치환 불가)
# - 숫자로 구성된 Series 적용 불가
# =============================================================================

s1.str.replace('a','A')
'''
0     Abcd
1    Abcde
2     AAbb
dtype: object
'''
['abcd','abcde','aaabb'].str.replace('a','A') # list는 안됨
# AttributeError: 'list' object has no attribute 'str'
DataFrame(['abcd','abcde','aaabb']).str.replace('a','A') # DF도 안됨
# AttributeError: 'DataFrame' object has no attribute 'str'
'''  df
       0
0   abcd
1  abcde
2  aaabb
'''

# =============================================================================
# pandas replace
# - pandas 제공
# - 값 치환 메서드(똑같은, 완전히 일치하는 값을 다른값으로 대체, 삭제)
# - Series, DataFrame 호출 가능
# - 숫자, NaN 치환 가능
# - 동시에 여러 대상 수정 가능
# =============================================================================

df1 = DataFrame([['1,200','1,300'],['1,400','1,500']])
'''
       0      1
0  1,200  1,300
1  1,400  1,500
'''
df1.replace(',','')         # 변화없음
'''
       0      1
0  1,200  1,300
1  1,400  1,500
'''

df2 = DataFrame([['1,200',','],['1,400','1,500']])
'''
       0      1
0  1,200      ,
1  1,400  1,500
'''
df2.replace(',','')         # 완전히 일치하는 데이터만 삭제됨
'''
       0      1
0  1,200       
1  1,400  1,500
'''

df3 = DataFrame([['1200','1300'],['1400','.']], columns = ['a','b'])
'''
      a     b
0  1200  1300
1  1400     .
'''
df3.replace('.',np.nan)
'''
      a     b
0  1200  1300
1  1400   NaN
'''

df3.replace(['.','1400','?','!'], np.nan) # NaN값으로도 변경 가능, 여러대상 가능
'''
      a     b
0  1200  1300
1   NaN   NaN
'''

# 연습) df1에 천단위 구분기호 제거 후, 모든 숫자 int 변경
df1 = DataFrame([['1,200','1,300'],['1,400','1,500']])
df1.replace(',','') # X 변화 없음
df1.str.replace(',','')
# AttributeError: 'DataFrame' object has no attribute 'str'

# DataFrame - applymap 사용
df1.applymap(lambda x: int(x.replace(',','')))
# 정수로 먼저 바꾸고 -> 매핑 // scalar는 str아닌 int로 변경해야 함
'''
      0     1
0  1200  1300
1  1400  1500
'''
df1.applymap(lambda x: int(x.replace(',',''))).sum() # df의 데이터타입 확인용
'''
0    2600
1    2800
dtype: int64
'''

df1.str.replace(',','').astype('int64')
# AttributeError: 'DataFrame' object has no attribute 'str'
# 학생답1

copy_df1 = df1
for i in range(0, len(df1)):
    copy_df1[i] = df1[i].str.replace(',','')
print(copy_df1)
# 학생답 2

for i in range(len(df1)):
    if df1[i].all() != 'int':
        df1[i] = df1[i].str.replace(',','').astype('int')
    else:
        pass
print(df1)
# 학생답 3
# =============================================================================
# 학생답 3 -> 쉽게?
for i in range(len(df1)):
    df1[i] = df1[i].replace(',','').astype('int')
print(df1)
# =============================================================================
df1[0]
'''
0    1200
1    1400
Name: 0, dtype: int32
'''
len(df1) # 2






