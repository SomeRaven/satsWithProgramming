import random
import psutil
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Memory monitoring function
def check_memory():
    process = psutil.Process(os.getpid())
    memory_mb = process.memory_info().rss / 1024 / 1024
    print(f"Memory usage: {memory_mb:.2f} MB")
    return memory_mb

print("=== Starting script ===")
check_memory()

list1 = [1,2,3,4,5,6]

#                       From, how many picks
sample1 = random.sample(list1, 1)
print(f"sample1: {sample1}")

#                       From, how many picks but with a k
sample2 = random.choices(list1, k=2)
print(f"sample2: {sample2}")

sample3 = random.choice(list1)
print(f"sample3: {sample3}")

# Demonstration of the difference
print("\n=== Demonstrating the difference ===")
print("random.sample() - no duplicates:")
for i in range(5):
    print(f"  {random.sample(list1, 3)}")

print("\nrandom.choices() - allows duplicates:")
for i in range(5):
    print(f"  {random.choices(list1, k=3)}")

print(f"\n=== Loading pandas data ===")
check_memory()

try:
    data = pd.read_csv('penguins_size.csv')
    print("Data loaded successfully!")
    check_memory()
    
    print(f"\nColumns: {list(data.columns)}")
    print(f"\nNull values per column:\n{data.isnull().sum()}")
    print(f"\nOriginal data length: {len(data)}")
    
    data1 = data.dropna()
    print(f"\nAfter dropping nulls:")
    print(f"Null values: {data1.isnull().sum().sum()}")
    print(f"New data length: {len(data1)}")
    print(f"Rows removed: {len(data) - len(data1)}")
    
    print(f"\n=== Final memory usage ===")
    final_memory = check_memory()
    
    # Data info
    print(f"\nData shape: {data1.shape}")
    print(f"Memory usage by pandas dataframe: {data1.memory_usage(deep=True).sum() / 1024 / 1024:.2f} MB")

except FileNotFoundError:
    print("penguins_size.csv not found in current directory")
    print("Make sure the file is in your ~/school/fall25 folder")
    check_memory()
except Exception as e:
    print(f"Error: {e}")
    check_memory()