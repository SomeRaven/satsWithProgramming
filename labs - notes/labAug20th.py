import pandas as pd
import numpy as np
import matplotlib
import seaborn as sns

data = sns.load_dataset('penguins')

print("----------------------------------")


print(data)
print("----------------------------------")

print(data.columns)
print("----------------------------------")
print(data.dtypes)
print("----------------------------------")

print(data.shape)
print("----------------------------------")

print(data.isnull().sum())