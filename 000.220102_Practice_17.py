# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 20:35:07 2022

@author: nnk
"""

run my_modules
# 날짜
from datetime import datetime
datetime.now()

d1 = datetime.now()
type(d1)
d1.year
d1.month
d1.day


# 날짜 파싱 str -> date
d2 = '2022/01/02'
d2.year # xx
datetime.strptime(d2,'%Y/%m/%d')

d3 = '2022-01-02'
datetime.strptime(d3,'%Y-%m-%d')

datetime.strptime('09/12/25', '%y/%m/%d')
datetime.strptime('09/12/25', '%m/%d/%y')


# Series 벡터연산 불가
s1 = Series(['2022/01/01','2022/01/02','2022/01/03'])
s1.map(lambda x: datetime.strptime(x, '%Y/%m/%d'))

# pd.to_datetime 벡터연산 가능
s2= pd.to_datetime(s1)
pd.to_datetime(s1,format='%Y/%m/%d')

s3 = pd.DataFrame({'date' : ['01-05-21','01-06-21','01-07-21',]})
s3.dtypes
# pd.to_datetime(s3,format='%Y-%m-%d') 안되는뎅?

# 날짜 포맷 변경 (str format time)
d1
datetime.strftime(d1, '%a')
datetime.strftime(d1, '%A')
datetime.strftime(d1, '%m-%d,%Y')
datetime.strftime(d1, '%Y')
datetime.strftime(d1, '%y')

s2 # 판다스로 datetime화 됨
datetime.strftime(s2,'%Y') # 안됨
s2.map(lambda x: datetime.strftime(x,'%Y'))

# 날짜 연산
d1 +100

# 1. offset
from pandas.tseries.offsets import Day, Hour, Second
d1 + Day(100)
# Timestamp('2022-04-12 20:36:13.434492')

# 2. timedelta (날짜와의 차이)
from datetime import timedelta
d1 + timedelta(100)
# datetime.datetime(2022, 4, 12, 20, 36, 13, 434492)

# 3. DateOffset *************************** 실무용***
d1 + pd.DateOffset(months=4)
# Timestamp('2022-05-02 20:36:13.434492')

# 4. 날짜 - 날짜
d3 = d1 - datetime.strptime(d2, '%Y/%m/%d')
d3.days
d3.seconds


# 연습) 요일별 통화건 수 총합
deli = pd.read_csv('./data/delivery.csv', encoding='cp949')
deli.dtypes
deli.head()
deli.info()
deli.describe()
# deli.boxplot()
deli['일자']
type(deli['일자'])
deli['일자'] = pd.to_datetime(deli['일자'], format='%Y%m%d')
# datetime.strftime(deli['일자'],'%A')
deli['요일'] = deli['일자'].map(lambda x: datetime.strftime(x,'%A'))

total = deli.groupby('요일')['통화건수'].sum()
total[['Monday', 'Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']]

# 일자별 통화건수 총합
deli.groupby('일자')['통화건수'].sum()


