# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 22:32:46 2021

@author: nnk
"""

# =============================================================================
# 13. merge vs. concat
# 행이 서로 분리되어 있는 하나의 데이터프레임으로 합치기  
# 컬럼이 서로 분리되어 있는 하나의 데이터프레임으로 합치기
# 참조 조건 사용, 연관된 두 데이터를 병합(join)
# =============================================================================

import pandas as pd
import numpy as np
from pandas import Series, DataFrame

df1 = DataFrame(np.arange(1,7).reshape(2,3),columns=['A','B','C'])
#    A  B  C
# 0  1  2  3
# 1  4  5  6
df2 = DataFrame(np.arange(10,61,10).reshape(2,3),columns=['A','B','C'])
#     A   B   C
# 0  10  20  30
# 1  40  50  60

# concat : concatenate 잇다
pd.concat([df1,df2])                # 각 DF의 인덱스 그대로 붇여넣기
#     A   B   C
# 0   1   2   3
# 1   4   5   6
# 0  10  20  30
# 1  40  50  60
pd.concat([df1,df2], ignore_index=True)     # 각 DF의 인덱스 무시하고 붙여넣기
#     A   B   C
# 0   1   2   3
# 1   4   5   6
# 2  10  20  30
# 3  40  50  60

# axis 설정
pd.concat([df1,df2], axis=0)        # 세로방향으로 합쳐짐 (default)
#     A   B   C
# 0   1   2   3
# 1   4   5   6
# 0  10  20  30
# 1  40  50  60
pd.concat([df1,df2], axis=1)        # 가로방향으로 합쳐짐 (열의 결합)
#    A  B  C   A   B   C
# 0  1  2  3  10  20  30
# 1  4  5  6  40  50  60


# =============================================================================
# 조인 (merge)
# 두 데이터프레임(테이블) 참조조건 활용, 하나의 객체로 합치거나 데이터를 처리하는 행위
# merge가 두 데이터 프레임 조인을 수행, 등가 조건만을 사용하여 조인이 가능
# =============================================================================

# 세팅
# RDBMS 관계형 데이터 베이스 관리 시스템
emp = pd.read_csv('./data/emp.csv')
#    empno  ename  deptno   sal
# 0      1  smith      10  4000
# 1      2  allen      10  4500
# 2      3   ford      20  4300
# 3      4  grace      10  4200
# 4      5  scott      30  4100
# 5      6   king      20  4000
df_dept = DataFrame({'deptno':[10,20,30], 'dname':['인사부','총무부','IT분석팀']})
#    deptno  dname
# 0      10    인사부
# 1      20    총무부
# 2      30  IT분석팀

# =============================================================================
# merge
# pd.merge(left,             # 첫번째 데이터프레임
#          right,            # 두번째 데이터프레임
#          how='inner',      # 조인 방법(default = 'inner' )
#          on=,              # 조인하는 컬럼(컬럼명이 서로 같을 때) 
#          left_on=,         # 첫번째 데이터프레임 조인(컬럼명이 서로 다를 때)
#          right_on=)        # 두번째 데이터프레임 조인(컬럼명이 서로 다를 때)
# =============================================================================
pd.merge(emp, df_dept, on = 'deptno')
'''
   empno  ename  deptno   sal  dname
 0      1  smith      10  4000    인사부
 1      2  allen      10  4500    인사부
 2      4  grace      10  4200    인사부
 3      3   ford      20  4300    총무부
 4      6   king      20  4000    총무부
 5      5  scott      30  4100  IT분석팀
'''
pd.merge(emp, df_dept, how='outer', on = 'deptno') # 크가 작아서 차이가 없음
# outer 조인을 더 많이 씀
pd.merge(emp, df_dept, how='left', on = 'deptno') # 크가 작아서 차이가 없음
# 왼쪽 df 기준으로 오른쪽결측은 삭제됨
pd.merge(emp, df_dept, how='right', on = 'deptno') # 크가 작아서 차이가 없음
# 오른쪽 df 기준으로 왼쪽결측은 삭제됨


# outer 조인
df_dept_new = DataFrame({'deptno':[10,20],'dname':['인사총무부','IT분석팀']})
#    deptno  dname
# 0      10  인사총무부
# 1      20  IT분석팀

pd.merge(emp,df_dept_new,on='deptno')               # 결측치 제외 조인값 출력
#    empno  ename  deptno   sal  dname
# 0      1  smith      10  4000  인사총무부
# 1      2  allen      10  4500  인사총무부
# 2      4  grace      10  4200  인사총무부
# 3      3   ford      20  4300  IT분석팀
# 4      6   king      20  4000  IT분석팀
pd.merge(emp,df_dept_new,how='outer',on='deptno')   # 결측치도 출력
#    empno  ename  deptno   sal  dname
# 0      1  smith      10  4000  인사총무부
# 1      2  allen      10  4500  인사총무부
# 2      4  grace      10  4200  인사총무부
# 3      3   ford      20  4300  IT분석팀
# 4      6   king      20  4000  IT분석팀
# 5      5  scott      30  4100    NaN
pd.merge(emp,df_dept_new,how='left',on='deptno')   # 첫번째 DF 기준 조인 출력
#    empno  ename  deptno   sal  dname
# 0      1  smith      10  4000  인사총무부
# 1      2  allen      10  4500  인사총무부
# 2      3   ford      20  4300  IT분석팀
# 3      4  grace      10  4200  인사총무부
# 4      5  scott      30  4100    NaN
# 5      6   king      20  4000  IT분석팀
pd.merge(emp,df_dept_new,how='right',on='deptno')   # 두번째 DF 기준 조인 출력
#    empno  ename  deptno   sal  dname
# 0      1  smith      10  4000  인사총무부
# 1      2  allen      10  4500  인사총무부
# 2      4  grace      10  4200  인사총무부
# 3      3   ford      20  4300  IT분석팀
# 4      6   king      20  4000  IT분석팀