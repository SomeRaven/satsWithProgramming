import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class C:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

data = pd.read_csv('CSVS/penguins_size.csv')
data = data.dropna()

data.columns

mean = np.mean(data["culmen_length_mm"])
print(f"{C.BLUE}mean: {mean}")
std = np.std(data["culmen_length_mm"])
print(f"std: {std}")
var1 = np.var(data["culmen_length_mm"])
print(f"variance: {var1} {C.END}")
percent = np.percentile(data['culmen_length_mm'], q=.75)
print(percent)

print(data.describe())

# plt.plot(data.describe())
# plt.show()

data_but_red = pd.read_csv('CSVS/repo_activity.csv')

team_avg = data_but_red.groupby("team")['commits'].mean()

print(team_avg)
plt.bar(team_avg.index, team_avg.values)
plt.show()
