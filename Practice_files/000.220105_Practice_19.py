# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 20:49:38 2022

@author: nnk
"""

run my_modules

df = pd.read_csv('./data/cancer_test.csv')
df.head()
-----
df.info()
# df.columns
# df.dtypes
-----
df.describe() # 갯수, 평균, 표준편차, 4쿼타일 값 확인

# 1.radius_mean, texture_mean, texture_se, smoothness_se
# NA인 행을 제거한 후 총 행의 수 리턴
df['radius_mean'].isnull().sum()
df['texture_mean'].isnull().sum()
df['texture_se'].isnull().sum()
df['smoothness_se'].isnull().sum()

vbool = df['radius_mean'].isnull() & df['texture_mean'].isnull() & df['texture_se'].isnull() & df['smoothness_se'].isnull()
vbool.sum()

df.loc[vbool,:]

df.shape
# df.shape[0]
# df.shape[1]

df.shape[0] - vbool.sum()
# print(df.shape[0] - vbool.sum())


# dropna
df.dropna(subset=['radius_mean','texture_mean','texture_se','smoothness_se'], how='all')
nrow = df.dropna(subset=['radius_mean','texture_mean','texture_se','smoothness_se'], how='all').shape[0]


# 2. concavity_mean의 standard scaling(표준화)
# 결과가 0.1 이상인 값의 개수
# =============================================================================
# standard scaling(표준화) = (원 데이터 - 평균)/표준편차
# minmax scaling = (원 데이터 - 최소) / (최대-최소) : 시계열 분석에서 잘씀
# =============================================================================

vscale = (df['concavity_mean']-df['concavity_mean'].mean())/df['concavity_mean'].std()
(vscale > 0.1).sum()


# 이상치 건 수 확인
# 3. texture_se 의 상위 10% 값 (NA를 제외한 건수의 10%)을 이상치로 가정
#   10%를 제외한 값의 최대값으로 수정한 후 평균을 소수점 둘째자리로 반올림하여 출력

df['texture_se'].dropna().shape[0]
nx = int(np.trunc(df['texture_se'].dropna().shape[0]*0.1))

vrank = df['texture_se'].rank(ascending=False, method='first')

df.loc[vrank>nx,'texture_se']
vmax = df.loc[vrank>nx,'texture_se'].max()

df['texture_se'].sort_values(ascending=False)[:nx]
df['texture_se'].sort_values(ascending=False)[:nx] = vmax

df['texture_se'].mean()
round(df['texture_se'].mean(),2)

# 4. symmetry_mean의 결측치를 최소값으로 수정한 후, 평균을 소수점 둘째자리로 반올림하여 출력
df['symmetry_mean'].min()
from numpy import nan as NA
df['symmetry_mean'] = df['symmetry_mean'].replace('-',NA)
df['symmetry_mean'] = df['symmetry_mean'].astype('float')
df['symmetry_mean'] = df['symmetry_mean'].replace('.',NA)
df['symmetry_mean'] = df['symmetry_mean'].replace('pass',NA)
df['symmetry_mean'] = df['symmetry_mean'].astype('float')

vmin = df['symmetry_mean'].astype('float').min()
df['symmetry_mean'] = df['symmetry_mean'].fillna(vmin)

print(round(df['symmetry_mean'].mean(),2))
