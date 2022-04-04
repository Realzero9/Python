# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 18:05:26 2021

@author: nnk
"""

v1 = 'abcde'
v2 = v1.upper()  # 'ABCDE'
v2.lower()  # 'abcde'
'abc def'.title()  # 'Abc Def' : camel 표기법

'abcd'[0]  # 'a'
'abcd'[-2]  # 'c'
'abcd'[0:3]  # 'abc'


vtel = '031)345-0834'
vtel[0:3]  # '031'

v1  # 'abcde'
v1.startswith('b')  # False
v1.startswith('b', 1)  # True
v1[1:].startswith('b')  # True

v1  # 'abcde'
v1.endswith('e') # True
v1.endswith('E') # False

'abc' == 'abc' # True
' abc '.strip() # 'abc'

'abc'.strip('a') #'bc'
'abaca'.strip('a') #'bac'

' bacd '.lstrip() # 'bacd '
' bacd '.rstrip() # ' bacd'

'abcabc'.replace('a','A') # 'AbcAbc'
'abcabc'.replace('ab','AB') # 'ABcABc'
'abcabc'.replace('ab','') # 'cc'

v11 = 'abcabc'
v11.replace('a','A') # 'AbcAbc'
# 같은 결과

'a/b/c/d'.split('/') # ['a', 'b', 'c', 'd']

v12= 'a/b/c/d'
v12.split('/') # ['a', 'b', 'c', 'd']

v122= ['a/b/c/d']
v122.split('/') 
# AttributeError: 'list' object has no attribute 'split'
v12.split('/')[1] # 'b'
v12.split('/')[0:2] # ['a', 'b']



v1 # 'abcde'
v1.find('b') # 1

vnum = vtel.find(')') # 3
vtel[0:vnum] # '031'
vtel[:vnum] # '031'


v13 = 'abcabcabc'
v13.count('a') # 3

type(v1) # str
v1.isalpha() # True
v1.isnumeric() # False
v1.isupper() # False
v1.islower() # True

'a' +'b' # 'ab'

len(v1) # 5
3/len(v1) # 0.6

vname = 'zero'
vemail = 'zero@naver.com'
jumin = '900909-1234567'

vname[1] == 'm' # False
vname.startswith('m',1) # False
vname.startswith('e',1) # True

vemail[:4] # 'zero'
idx = vemail.find('@') # 4
vemail[:idx] # 'zero'

jumin.split('-')[1][0] # 1
jumin.split('-')[1][0] == '2' # False
jumin[7] # 1
