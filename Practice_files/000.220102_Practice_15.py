# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 20:04:41 2022

@author: nnk
"""

# stack, unstack, pivot_table

run my_modules
kimchi = pd.read_csv('./data/kimchi_test.csv', encoding='cp949')
df1 = kimchi.groupby(['판매년도','제품'])[['수량']].sum(0)

df2 = df1.unstack()
df2 = df1.unstack(level=0)
df2 = df1.unstack(level=1)

# pivot_table
kimchi.pivot_table(index='판매년도',
                   columns='제품',values='판매금액',aggfunc='sum')
