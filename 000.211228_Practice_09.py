# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 22:45:04 2021

@author: nnk
"""

import numpy as np
from pandas import Series, DataFrame

# =============================================================================
# 산술연산 메서드
# =============================================================================
df1 = DataFrame(np.arange(1,17).reshape(4,4))
'''
    0   1   2   3
0   1   2   3   4
1   5   6   7   8
2   9  10  11  12
3  13  14  15  16
'''
dir(df1)
df1.sum(axis=0)             # 서로다른 행끼리 더함
'''
0    28
1    32
2    36
3    40
dtype: int64
'''
df1.sum(axis=1)             # 서로다른 열끼리 더함
'''
0    10
1    26
2    42
3    58
dtype: int64
'''

df1.iloc[:,0]
'''
0     1
1     5
2     9
3    13
Name: 0, dtype: int32
'''
df1.iloc[:,0].sum() # 28
df1.iloc[:,0].mean() # 7.0

df1.iloc[0,0] =np.nan
'''
      0   1   2   3
0   NaN   2   3   4
1   5.0   6   7   8
2   9.0  10  11  12
3  13.0  14  15  16
'''
df1.iloc[:,0].mean() # 9.0 : NaN 무시하고 연산
# skipna = True (default)


# 평균값(최대 또는 최소) 대치
df1.iloc[:,0].isnull()
'''
0     True
1    False
2    False
3    False
Name: 0, dtype: bool
'''
df1.iloc[:,0][df1.iloc[:,0].isnull()] = df1.iloc[:,0].mean()
# 널값이 있으면 그 열의 평균값으로 대치
'''
      0   1   2   3
0   9.0   2   3   4
1   5.0   6   7   8
2   9.0  10  11  12
3  13.0  14  15  16
'''

df1[df1.isnull()]
df1[df1.notnull()]

df1.iloc[:,0].var()  # 10.666666666666666 >> 분산
df1.iloc[:,0].std()  # 3.265986323710904 >> 표준편차
df1.iloc[:,0].min()  # 5.0 >> 최소값
df1.iloc[:,0].max()  # 13.0 >> 최대값
df1.iloc[:,0].median()  # 9.0 >> 중위수(중앙값)

df1.iloc[:,0] >= 10
'''
0    False
1    False
2    False
3     True
Name: 0, dtype: bool
'''
(df1.iloc[:,0]>=10).sum() # True의 갯수
