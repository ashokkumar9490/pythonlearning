""" pasdas demo """

import pandas as pd

df = pd.read_csv('data2.csv')

# df['Date'] = pd.to_datetime(df['Date'], format='%Y/%m/%d')    # 20201226
df['Date'] = pd.to_datetime(df['Date'], format='mixed')    # 20201226

print(df.to_string())
