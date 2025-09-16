import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""
Name: Kyleigh Hill
Date: Sept 15th, 2025
Time Started: Saturday Sept 13th 3:00pm
Time Finished: Monday Sept 15th 4:32pm
Concepts needed to go over moving forward: 
    - task 4 Person vs Spearman 
"""

sProductivity = pd.read_csv("CSVS/student_productivity.csv")

head1 = sProductivity.head()
tail1 = sProductivity.tail()
info = sProductivity.info()
desc = sProductivity.describe()

print(f"head: \n {head1} \n tail: \n {tail1} \n info: \n {info} \n desc: {desc}")

data_types = sProductivity.dtypes
print(f"Data Types: {data_types}")

shape = sProductivity.shape
print(f"Shape: {shape}")

numNull = sProductivity.isnull().sum()
print(f"Total of null values: \n{numNull}")

# task 1 scatterplots with regression lines
plt.scatter(sProductivity['study_hours_per_week'], sProductivity['exam_score'])
sns.regplot(data=sProductivity, x='study_hours_per_week', y='exam_score', scatter=False, color='red')
plt.title('study hours vs exam score')
plt.show()

plt.scatter(sProductivity['social_media_hours_per_day'], sProductivity['assignment_score'])
sns.regplot(data=sProductivity, x='social_media_hours_per_day', y='assignment_score', scatter=False, color='red')
plt.title('social media vs assignment score')
plt.show()

plt.scatter(sProductivity['sleep_hours_per_night'], sProductivity['stress_level'])
sns.regplot(data=sProductivity, x='sleep_hours_per_night', y='stress_level', scatter=False, color='red')
plt.title('sleep vs stress')
plt.show()

# task 2 correlations
corr_matrix = sProductivity.corr()
print(corr_matrix)

sns.heatmap(corr_matrix, annot=True)
plt.show()

# strongest correlations 
print(f"strongest positive: {corr_matrix.max().max():.3f}")
print(f"strongest negative: {corr_matrix.min().min():.3f}")

# task 3 
study_exam = sProductivity['study_hours_per_week'].corr(sProductivity['exam_score'])
print(f"study vs exam: {study_exam:.3f}")

social_assign = sProductivity['social_media_hours_per_day'].corr(sProductivity['assignment_score'])
print(f"social media vs assignment: {social_assign:.3f}")

attend_exam = sProductivity['class_attendance_pct'].corr(sProductivity['exam_score'])
print(f"attendance vs exam: {attend_exam:.3f}")

if study_exam > attend_exam:
    print("study hours better")
else:
    print("attendance better")

# task 4 (Need to look into what this really is.)
stress_sleep_df = sProductivity[['stress_level', 'sleep_hours_per_night']]
spearman_stress_sleep = stress_sleep_df.corr(method='spearman').iloc[0,1]
print(f"spearman stress sleep: {spearman_stress_sleep:.3f}")

pearson_study_exam = sProductivity['study_hours_per_week'].corr(sProductivity['exam_score'])
study_exam_df = sProductivity[['study_hours_per_week', 'exam_score']]
spearman_study_exam = study_exam_df.corr(method='spearman').iloc[0,1]
print(f"pearson study exam: {pearson_study_exam:.3f}")
print(f"spearman study exam: {spearman_study_exam:.3f}")

# task 5
print("\ncorrelations with assignment:")
print(f"study hours: {sProductivity['study_hours_per_week'].corr(sProductivity['assignment_score']):.3f}")
print(f"sleep: {sProductivity['sleep_hours_per_night'].corr(sProductivity['assignment_score']):.3f}")
print(f"attendance: {sProductivity['class_attendance_pct'].corr(sProductivity['assignment_score']):.3f}")
print(f"social media: {sProductivity['social_media_hours_per_day'].corr(sProductivity['assignment_score']):.3f}")
print(f"stress: {sProductivity['stress_level'].corr(sProductivity['assignment_score']):.3f}")

print("\ncorrelations with exam:")
print(f"study hours: {sProductivity['study_hours_per_week'].corr(sProductivity['exam_score']):.3f}")
print(f"sleep: {sProductivity['sleep_hours_per_night'].corr(sProductivity['exam_score']):.3f}")
print(f"attendance: {sProductivity['class_attendance_pct'].corr(sProductivity['exam_score']):.3f}")
print(f"social media: {sProductivity['social_media_hours_per_day'].corr(sProductivity['exam_score']):.3f}")
print(f"stress: {sProductivity['stress_level'].corr(sProductivity['exam_score']):.3f}")