""" pasdas demo """

import pandas as pd

# df = pd.read_csv('data.csv')

# print(df)
# print(pd.options.display.max_rows)  # 60 lines
pd.options.display.max_rows = 200

# print(df)


# print(df.head(20))
# print("-------------")
# print(df.tail())


# print(df.info())


df = pd.read_csv('data.csv')
# new_df = df.dropna()
# print(new_df)


df.fillna(130, inplace=True)
print(df)
