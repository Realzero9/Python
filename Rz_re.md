# 정규식

- import re 
  글자를 다루는 모듈

- 정규식: 문자,글자를 다루는 식

- https://wikidocs.net/4308 참고

- tags = re.findall(r'#\w+', content)
  - r: 문자그대로, \w+ 단어전체

- tags = re.findall(r'#[\^\s#,\\]+', content)
  - \s 스페이스



# 빈도수 집계

- from collections import Counter
  - 딕셔너리 형식으로 세어줌
- pandas.value_counts()
  - pandas도 갯수 세기 가능
- pivot_table()
  - Series, df 타입으로 만들수있음