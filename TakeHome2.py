# David Huang
# Data Science Take Home #2

import pandas as pd
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
print(df[df.index % 20 == 0]["Manufacturer"] + " " +  df[df.index % 20 == 0]["Model"] + " " + df[df.index % 20 == 0]["Type"])

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
df["Min.Price"] = df["Min.Price"].fillna(df["Min.Price"].mean())
df["Max.Price"] = df["Max.Price"].fillna(df["Max.Price"].mean())
print(df) 

df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
print(df)
sum = df.sum(axis=1)
print(sum > 100)

arr = np.random.randint(1, 100, size=(4, 4))
print(arr)
arr_col = arr.reshape((16, 1))
arr_row = arr.reshape((1, 16))
print(arr_col)
print(arr_row)
arr_col_sum = lambda arr : np.sum(arr, axis=0)
arr_row_sum = lambda arr : np.sum(arr, axis=1)
print(arr_col_sum(arr))
print(arr_row_sum(arr))


