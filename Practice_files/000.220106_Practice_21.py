# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 20:05:42 2022

@author: nnk
"""

run my_modules

# 결측치 처리
df1 = pd.read_csv('./data/file1.txt')

# [ 문제 ]
# df1의 a컬럼의 결측치를 a컬럼의 최소값으로 대치 후 전체 평균 계산

df1['a'].astype('float') # 일단 실수로 바꿔보는데, 바꿀수없는 데이터타입이 있음
df1['a'][df1['a']=='.']
df1['a'][df1['a']=='.'] = np.nan
df1['a'] = df1['a'].astype('float')

# nan값을 제외한 최소값 확인하여 변수 저장
vmin = df1['a'].min()

df1['a'].isnull()
df1['a'][df1['a'].isnull()] = vmin
df1['a'].mean()

# 이상치 : 범위를 벗어난 데이터
# [문제]
# df1의 d컬럼을 보세요. d컬럼의 경우 16이상인 경우를 이상치로 판단할 거예요
# 이상치를 제외한 나머지에 대해 최대값으로 이상치를 대치한 후, 평균을 계산하세요
df1['d']>=16
df1['d'][df1['d']>=16] # 이상치
vmax = df1['d'][df1['d']<16].max()

df1['d'][df1['d']>=16] = vmax

df1['d'].mean()

