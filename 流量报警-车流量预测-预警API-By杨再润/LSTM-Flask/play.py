#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/12/24 15:15
# @Author  : 杨再润
# @Site  :  https://tim-saijun.github.io/
import pandas as pd
df = pd.read_csv('data/data1.csv', encoding='utf-8')
#去掉每一列前11个字符和最后三个字符
df['Date'] = df['Date'].str[11:-3]
#将第二列重命名为LTZXZ,第三列重命名为SLDZ,第四列重命名为SSHN
df.rename(columns={'Open': 'LTZXZ', 'High': 'SLDZ', 'Close': 'SSHN'}, inplace=True)
print(df.head())
#将df存储为csv
df.to_csv('data/data2.csv', index=False, encoding='utf-8')
