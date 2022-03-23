# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 17:20:05 2021

@author: nnk
"""

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

pwd

emp = pd.read_csv('./data/emp.csv')
'''
   empno  ename  deptno   sal
0      1  smith      10  4000
1      2  allen      10  4500
2      3   ford      20  4300
3      4  grace      10  4200
4      5  scott      30  4100
5      6   king      20  4000
'''
# =============================================================================
# import os
# os.getcwd()
# =============================================================================

# 1. sort_index
# - Series, DataFrame 호출 가능
# - index, column 재배치

# 속성정보 뽑기
emp.ename
emp['ename']

emp.index = emp['empno'] # 인덱스 지정하기, 자료 그대로, 인덱스만 지정
'''
       empno  ename  deptno   sal
empno                            
1          1  smith      10  4000
2          2  allen      10  4500
3          3   ford      20  4300
4          4  grace      10  4200
5          5  scott      30  4100
6          6   king      20  4000
'''
emp.iloc[:,1:]
'''
       ename  deptno   sal
empno                     
1      smith      10  4000
2      allen      10  4500
3       ford      20  4300
4      grace      10  4200
5      scott      30  4100
6       king      20  4000
'''

emp = emp.set_index('ename') # 해당 열이 사라지고 idx로 사용
'''
       empno  deptno   sal
ename                     
smith      1      10  4000
allen      2      10  4500
ford       3      20  4300
grace      4      10  4200
scott      5      30  4100
king       6      20  4000
'''

emp.sort_index(ascending=True) # 인덱스 기준 오름차순 정렬
'''
       empno  deptno   sal
ename                     
allen      2      10  4500
ford       3      20  4300
grace      4      10  4200
king       6      20  4000
scott      5      30  4100
smith      1      10  4000
'''

emp.sort_index(ascending=False) # 인덱스 기준 내림차순 정렬
'''
       empno  deptno   sal
ename                     
smith      1      10  4000
scott      5      30  4100
king       6      20  4000
grace      4      10  4200
ford       3      20  4300
allen      2      10  4500
'''

emp.sort_index(axis=0)      # 행 기준, 행 순서대로 정렬
'''
       empno  deptno   sal
ename                     
allen      2      10  4500
ford       3      20  4300
grace      4      10  4200
king       6      20  4000
scott      5      30  4100
smith      1      10  4000
'''

emp.sort_index(axis=1)      # 열 기준, 열 순서대로 정렬
'''
       deptno  empno   sal
ename                     
smith      10      1  4000
allen      10      2  4500
ford       20      3  4300
grace      10      4  4200
scott      30      5  4100
king       20      6  4000
'''


# 2. sort_values
# - Series, DataFrame 호출 가능
# - 본문의 값(value)로 정렬 (Series, DataFrame 특정 칼럼 순서대로)

emp.sort_values(by='sal')
emp.sort_values('sal')
'''
       empno  deptno   sal
ename                     
smith      1      10  4000
king       6      20  4000
scott      5      30  4100
grace      4      10  4200
ford       3      20  4300
allen      2      10  4500
'''

emp.sort_values('sal', ascending=False)
'''
       empno  deptno   sal
ename                     
allen      2      10  4500
ford       3      20  4300
grace      4      10  4200
scott      5      30  4100
smith      1      10  4000
king       6      20  4000
'''


## 부서별, 연봉수준 !!
emp.sort_values(by=['deptno', 'sal'])
'''
       empno  deptno   sal
ename                     
smith      1      10  4000
grace      4      10  4200
allen      2      10  4500
king       6      20  4000
ford       3      20  4300
scott      5      30  4100
'''

emp.sort_values(by=['deptno','sal'], ascending=[True, False])
'''
       empno  deptno   sal
ename                     
allen      2      10  4500
grace      4      10  4200
smith      1      10  4000
ford       3      20  4300
king       6      20  4000
scott      5      30  4100
'''