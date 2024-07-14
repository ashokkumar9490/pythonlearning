import numpy as np
import pandas as pd

# s1 = pd.Series([1, 3, 5, 7, 6, 8])
# print(s1)


# sales = pd.Series([100, 200, 100, 400], index=['Jan', 'Feb', 'Mar', 'Apr'])
# print(sales)


calories = {"day1": 420, "day2": 380, "day3": 390}
cal = pd.Series(calories)

c2 = cal + 2
print(c2)

# print(cal.sum())
# print(cal.mean())
# print(cal.std())
# print(cal.max())
# print(cal.min())
