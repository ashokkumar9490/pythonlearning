""" pasdas demo """
import os
import pandas as pd

df = pd.read_csv('data2.csv')

print(df)

# df['Date'] = pd.to_datetime(df['Date'], format='mixed')    # 20201226

# print(df.to_string())

# # print(os.getcwd())

# df.to_csv('data22.csv', index=False)
