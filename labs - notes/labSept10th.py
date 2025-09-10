import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sProductivity = pd.read_csv("../CSVS/student_productivity.csv")


head1 = sProductivity.head()

tail1 = sProductivity.tail()

info = sProductivity.info()

desc = sProductivity.describe()

print(f"head: \n {head1} \n tail: \n {tail1} \n info: \n {info} \n desc: {desc}")

data_types = sProductivity.dtypes

print(f"Data Types: {data_types}")

shape = sProductivity.shape

print(f"Shape: {shape}")

numNull = sProductivity.isnull().sum

print(f"Total of null values: {numNull}")

