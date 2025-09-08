import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

repo_data = pd.read_csv('CSVS/repo_activity.csv')
sprint_data = pd.read_csv('CSVS/sprint_metrics.csv')
ab_test_data = pd.read_csv('CSVS/ab_test_feature_flag.csv')

plt.hist(repo_data['code_churn'])
plt.title('code_churn')
plt.show()

plt.hist(sprint_data['lead_time_days'])
plt.title('lead_time_days')
plt.show()

plt.hist(ab_test_data['time_on_task_min'])
plt.title('time_on_task_min')
plt.show()

plt.scatter(repo_data['code_churn'],repo_data['build_success_rate'] )
plt.title('code churn vs build success')
plt.xlabel('code churn')
plt.ylabel('build success rate')
plt.show()

plt.scatter(sprint_data['incidents'], sprint_data['deployments'])
plt.title('incidents vs deployments')
plt.xlabel('incidents')
plt.ylabel('deployments')
plt.show()

plt.scatter(ab_test_data['time_on_task_min'], ab_test_data['revenue_usd'])
plt.title('time on task vs revenue')
plt.xlabel('time on task')
plt.ylabel('revenue')
plt.show()

# Step 1: Aggregate commits by team
team_commits = repo_data.groupby("team")["commits"].sum()

# Step 2: Calculate percentages
team_percent = (team_commits / team_commits.sum()) * 100

# Step 3: Plot as pie chart
plt.pie(team_percent, labels=team_percent.index, autopct="%.1f%%")
plt.title("Percentage of Total Commits by Team")
plt.show()

# Step 1: Group by week and repo
weekly_commits = repo_data.groupby(["week_start", "repo"])["commits"].sum().reset_index()

# Step 2: Pivot so repos become columns
commit_trends = weekly_commits.pivot(index="week_start", columns="repo", values="commits")

# Step 3: Plot line chart
commit_trends.plot(kind="line", marker="o")
plt.title("Weekly Commits by Repo")
plt.xlabel("Week")
plt.ylabel("Number of Commits")
plt.legend(title="Repo")
plt.grid(True)
plt.show()