# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

data = pd.read_excel('Data_coding_ver.xlsx')
# apply() 함수 : 1을 넣어라 0보다 크고 17.89보다 작으면, 아니면 2를 넣어라 x가 17.89보다 크고 22.34보다 작으면, 아니면 그냥 3을 넣어라
data['W101'] = data['W101'].apply(lambda x: 1 if 0<=x and x<17.89 else 2 if 17.89 <= x and x<22.34 else 3)
data['W102'] = data['W102'].apply(lambda x: 1 if 0<=x and x<157.83 else 2 if 157.83 <= x and x<213.25 else 3)
data['W103'] = data['W103'].apply(lambda x: 1 if 0<=x and x<21.19 else 2 if 21.19 <= x and x<27.75 else 3)
data['W104'] = data['W104'].apply(lambda x: 1 if 0<=x and x<155.36 else 2 if 155.36 <= x and x<206.54 else 3)
# print(data)
# 9번째에 W104위치함
data.insert(10, 'W101~W104 total', data['W101']+data['W102']+data['W103']+data['W104'])
print(data)