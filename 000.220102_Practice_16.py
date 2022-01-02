# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 20:20:28 2022

@author: nnk
"""

run my_modules
s1 = Series([1,2,3,np.nan])
s2 = Series(['a','b','c',np.nan])

# 대세에 영향을 주지않는 최빈값으로 수정
s1.mean()
s1.fillna(0)
s1[s1.isnull()]=0

s2.replace(np.nan,'a')

# na로 수정
s3 = Series(['서울','.','대전','.','대구','.','부산'])
s3 = s3.replace('.',np.nan)

# 앞/뒤 값으로 수정
s3.fillna(method='ffill')
s3.fillna(method='bfill')

s3.ffill()
s3.bfill()


# Na 행, 열 제거
df3 = DataFrame(np.arange(1,17).reshape(4,4), columns=list('ABCD'))
df3.iloc[0,0] = np.nan
df3.iloc[1,[0,1]] = np.nan
df3.iloc[2,[0,1,2]] = np.nan
df3.iloc[3,:] = np.nan

df3.dropna(how='all')
df3.dropna(thresh=2) # ********************
df3.dropna(axis=1, how='all')
df3.dropna(subset=['C']) # ****************

# 중복값처리
s1 = Series([1,1,2,3,4])
s1.unique()
s1.duplicated()
s1.drop_duplicates()

df5 = DataFrame({'A':[1,1,3,4], 'B':[10,10,30,40]})
df5.drop_duplicates()
df5.drop_duplicates(keep='last')

df6 = DataFrame({'A':[1,1,3,4], 'B':[10,10,30,40],'c':[100,200,300,400]})
df6.drop_duplicates()
df6.drop_duplicates(subset=['A','B'])
df6.drop_duplicates(subset=['A','B'],keep='last')
