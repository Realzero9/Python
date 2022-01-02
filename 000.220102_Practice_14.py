# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 18:39:49 2022

@author: nnk
"""

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

emp = pd.read_csv('./data/emp.csv')

# scott의 퇴사
emp['ename'] == 'scott'
emp.loc[emp['ename']=='scott']
emp.loc[~(emp['ename']=='scott'),:]

# 'sal'칼럼 제외
emp.drop(4, axis=0)
emp.drop('sal', axis=1)

emp.iloc[:,:3]
emp.iloc[:,:-1]
emp.loc[:,'empno':'deptno']

# 'sal'만 나오게
emp.drop(['ename','deptno'],axis=1)
emp.iloc[:,::3]



# shift
emp['sal']
emp['sal'].shift()
emp.shift(axis=1)

# 예제) 다음 데이터에서 전일자 대비 증감율 출력
# 증감율 = (오늘 - 전일) / 전일 * 100
s1 = Series([3000,3500,4200,2800,3600],
            index=['2021/01/01','2021/01/02','2021/01/03','2021/01/04','2021/01/05'])

s11 = s1.shift()
(s1 - s11)/s11*100 # 답


# rename
emp.columns=['emptno','ename','deptno','salary']
emp.rename({'salary':'sal','deptno':'dept_no'},axis=1)

# 예제) emp에서 ename을 idx로 설정, scott을 SCOTT으로 변경
emp.set_index('ename').rename({'scott':'SCOTT'},axis=0)
emp.index = emp['ename']
emp.rename({'scott':'SCOTT'},axis=0)
