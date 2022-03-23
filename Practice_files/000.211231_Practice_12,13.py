# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 18:41:49 2021

@author: nnk
"""

run my_modules

kimchi = pd.read_csv('./data/kimchi_test.csv', encoding='cp949')

# 예제1) 제품별, 판매처별 수량의 총 합
kimchi.groupby(by='제품').sum()
kimchi.groupby(by=['제품', '판매처']).sum()
kimchi.groupby(by=['제품', '판매처'])[['수량']].sum()

# 예제2) 제품 기준, 수량과 판매금액의 총합
kimchi.groupby(by='제품')[['수량','판매금액']].sum()

# agg : 여러 함수를 동시에 전달
# 예제3) 제품별, 판매처별 수량의 총 합과 평균
kimchi.groupby(by=['제품', '판매처'])[['수량']].agg(['sum','mean'])

# 예제4) 제품별, 판매처별 수량의 총합, 판매금액의 평균 >> dict() 사용
kimchi.groupby(by=['제품','판매처'])[['수량','판매금액']].agg({'수량':'sum', '판매금액':'mean'})


# 멀티레벨을 갖는 경우의 groupby 연산
kimchi_2 = kimchi.groupby(by=['제품','판매처'])[['수량']].sum()

# 1. 제품별 총합
kimchi_2.groupby(level=0).sum()
# = kimchi_2.groupby(by='제품')).sum()

# 2. 판매처별 총합
kimchi_2.groupby(level=1).sum()



# =============================================================================
# 13. merge vs. concat
# 행이 서로 분리되어 있는 하나의 데이터프레임으로 합치기  
# 컬럼이 서로 분리되어 있는 하나의 데이터프레임으로 합치기
# 참조 조건 사용, 연관된 두 데이터를 병합(join)
# =============================================================================

df1 = DataFrame(np.arange(1,7).reshape(2,3),columns=['A','B','C'])
df2 = DataFrame(np.arange(10,61,10).reshape(2,3),columns=['A','B','C'])

# concat
pd.concat([df1,df2])
pd.concat([df1,df2], ignore_index=True)

# axis
pd.concat([df1,df2], axis=0)
pd.concat([df1,df2], axis=1)

# merge
emp = pd.read_csv('./data/emp.csv')
df_dept = DataFrame({'deptno':[10,20,30], 'dname':['인사부','총무부','IT분석팀']})

pd.merge(emp, df_dept, on='deptno')
'''
   empno  ename  deptno   sal  dname
0      1  smith      10  4000    인사부
1      2  allen      10  4500    인사부
2      4  grace      10  4200    인사부
3      3   ford      20  4300    총무부
4      6   king      20  4000    총무부
5      5  scott      30  4100  IT분석팀
'''

# outer 조인
df_dept_new = DataFrame({'deptno':[10,20],'dname':['인사총무부','IT분석팀']})

pd.merge(emp, df_dept_new, on='deptno') # 기본
pd.merge(emp, df_dept_new, how='outer', on='deptno') # outer, 결측치 출력
pd.merge(emp, df_dept_new, how='left', on='deptno') # 앞df기준정렬 출력
pd.merge(emp, df_dept_new, how='right', on='deptno') # 뒤df기준정렬 출력



