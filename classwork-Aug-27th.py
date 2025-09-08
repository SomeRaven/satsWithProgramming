import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


repo_data = pd.read_csv('CSVS/repo_activity.csv')
sprint_data = pd.read_csv('CSVS/sprint_metrics.csv')
ab_test_data = pd.read_csv('CSVS/ab_test_feature_flag.csv')

plt.hist(repo_data['code_churn'], bins=15, alpha=0.7, edgecolor='black')
plt.xlabel('Code Churn')
plt.ylabel('Frequency')
plt.title('Distribution of Code Churn Across All Repos')
plt.show()

plt.hist(sprint_data['lead_time_days'], bins=10, alpha=0.7, edgecolor='black')
plt.xlabel('Lead Time (Days)')
plt.ylabel('Frequency')
plt.title('Distribution of Lead Time Across All Sprints')
plt.show()


plt.hist(ab_test_data['time_on_task_min'], bins=30, alpha=0.7, edgecolor='black', color='skyblue')
plt.xlabel('Time on Task (Minutes)')
plt.ylabel('Number of Users')
plt.title('Distribution of Time on Task Among Users')
plt.grid(True, alpha=0.3)
plt.show()
