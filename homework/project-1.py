import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# load datasets
student_data = pd.read_csv("../CSVS/student_performance.csv")
hospital_data = pd.read_csv("../CSVS/hospital_readmission.csv")

print("STUDENT DATASET")
print("="*50)

head1 = student_data.head()
tail1 = student_data.tail()
info = student_data.info()
desc = student_data.describe()

print(f"head: \n {head1} \n tail: \n {tail1} \n info: \n {info} \n desc: {desc}")

data_types = student_data.dtypes
print(f"Data Types: {data_types}")

shape = student_data.shape
print(f"Shape: {shape}")

numNull = student_data.isnull().sum()
print(f"Total of null values: \n{numNull}")

# task 1 - descriptive stats for each variable
print("\nDESCRIPTIVE STATS:")
for column in student_data.columns:
    if column != 'ID':
        if student_data[column].dtype == 'object':
            print(f"\n{column} (categorical):")
            print(student_data[column].value_counts())
        else:
            print(f"\n{column}:")
            print(f"mean: {student_data[column].mean():.2f}")
            print(f"median: {student_data[column].median():.2f}")
            print(f"std: {student_data[column].std():.2f}")
            print(f"min: {student_data[column].min():.2f}")
            print(f"max: {student_data[column].max():.2f}")

# histograms for numeric variables
numeric_cols = ['Age', 'StudyTime', 'Failures', 'Absences', 'G1', 'G2', 'G3']
for col in numeric_cols:
    plt.hist(student_data[col])
    plt.title(f'{col} distribution')
    plt.xlabel(col)
    plt.ylabel('frequency')
    plt.savefig(f'../graph_pictures/student_{col}_histogram.png', dpi=300, bbox_inches='tight')
    plt.close()

# bar chart for gender
plt.bar(student_data['Gender'].value_counts().index, student_data['Gender'].value_counts().values)
plt.title('gender distribution')
plt.savefig('../graph_pictures/student_gender_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

# task 2 - relationship of G3 with age, study time, absences by gender
print("\nTASK 2: G3 relationships by gender")

# separate data by gender - FIXED
boys = student_data[student_data['Gender'] == 'Male']
girls = student_data[student_data['Gender'] == 'Female']

print(f"boys count: {len(boys)}")
print(f"girls count: {len(girls)}")

# G3 vs Age by gender
plt.scatter(boys['Age'], boys['G3'], label='boys', alpha=0.6)
plt.scatter(girls['Age'], girls['G3'], label='girls', alpha=0.6)
sns.regplot(data=boys, x='Age', y='G3', scatter=False, label='boys trend')
sns.regplot(data=girls, x='Age', y='G3', scatter=False, label='girls trend')
plt.title('G3 vs Age by gender')
plt.xlabel('age')
plt.ylabel('final grade G3')
plt.legend()
plt.savefig('../graph_pictures/g3_vs_age_by_gender.png', dpi=300, bbox_inches='tight')
plt.close()

# G3 vs StudyTime by gender
plt.scatter(boys['StudyTime'], boys['G3'], label='boys', alpha=0.6)
plt.scatter(girls['StudyTime'], girls['G3'], label='girls', alpha=0.6)
sns.regplot(data=boys, x='StudyTime', y='G3', scatter=False, label='boys trend')
sns.regplot(data=girls, x='StudyTime', y='G3', scatter=False, label='girls trend')
plt.title('G3 vs study time by gender')
plt.xlabel('study time')
plt.ylabel('final grade G3')
plt.legend()
plt.savefig('../graph_pictures/g3_vs_studytime_by_gender.png', dpi=300, bbox_inches='tight')
plt.close()

# G3 vs Absences by gender
plt.scatter(boys['Absences'], boys['G3'], label='boys', alpha=0.6)
plt.scatter(girls['Absences'], girls['G3'], label='girls', alpha=0.6)
sns.regplot(data=boys, x='Absences', y='G3', scatter=False, label='boys trend')
sns.regplot(data=girls, x='Absences', y='G3', scatter=False, label='girls trend')
plt.title('G3 vs absences by gender')
plt.xlabel('absences')
plt.ylabel('final grade G3')
plt.legend()
plt.savefig('../graph_pictures/g3_vs_absences_by_gender.png', dpi=300, bbox_inches='tight')
plt.close()

# correlations by gender
print("correlations for boys:")
print(f"age vs G3: {boys['Age'].corr(boys['G3']):.3f}")
print(f"study time vs G3: {boys['StudyTime'].corr(boys['G3']):.3f}")
print(f"absences vs G3: {boys['Absences'].corr(boys['G3']):.3f}")

print("correlations for girls:")
print(f"age vs G3: {girls['Age'].corr(girls['G3']):.3f}")
print(f"study time vs G3: {girls['StudyTime'].corr(girls['G3']):.3f}")
print(f"absences vs G3: {girls['Absences'].corr(girls['G3']):.3f}")

# task 3 - grade progression G1 -> G2 -> G3
print("\nTASK 3: grade progression")

boys_grades = boys[['G1', 'G2', 'G3']].mean()
girls_grades = girls[['G1', 'G2', 'G3']].mean()

print("average grades progression:")
print(f"boys: G1={boys_grades['G1']:.2f}, G2={boys_grades['G2']:.2f}, G3={boys_grades['G3']:.2f}")
print(f"girls: G1={girls_grades['G1']:.2f}, G2={girls_grades['G2']:.2f}, G3={girls_grades['G3']:.2f}")

# plot grade progression
grades = ['G1', 'G2', 'G3']
plt.plot(grades, boys_grades, marker='o', label='boys')
plt.plot(grades, girls_grades, marker='o', label='girls')
plt.title('grade progression by gender')
plt.xlabel('exam')
plt.ylabel('average grade')
plt.legend()
plt.savefig('../graph_pictures/grade_progression_by_gender.png', dpi=300, bbox_inches='tight')
plt.close()

# boxplots for each grade by gender
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
student_data.boxplot(column='G1', by='Gender', ax=plt.gca())
plt.title('G1 by gender')

plt.subplot(1, 3, 2)
student_data.boxplot(column='G2', by='Gender', ax=plt.gca())
plt.title('G2 by gender')

plt.subplot(1, 3, 3)
student_data.boxplot(column='G3', by='Gender', ax=plt.gca())
plt.title('G3 by gender')

plt.tight_layout()
plt.savefig('../graph_pictures/grades_boxplots_by_gender.png', dpi=300, bbox_inches='tight')
plt.close()

print("\n" + "="*50)
print("HOSPITAL DATASET")
print("="*50)

head2 = hospital_data.head()
tail2 = hospital_data.tail()
info2 = hospital_data.info()
desc2 = hospital_data.describe()

print(f"head: \n {head2} \n tail: \n {tail2} \n info: \n {info2} \n desc: {desc2}")

data_types2 = hospital_data.dtypes
print(f"Data Types: {data_types2}")

shape2 = hospital_data.shape
print(f"Shape: {shape2}")

numNull2 = hospital_data.isnull().sum()
print(f"Total of null values: \n{numNull2}")

# task 1 - descriptive stats
print("\nDESCRIPTIVE STATS:")
for column in hospital_data.columns:
    if column != 'ID':
        if hospital_data[column].dtype == 'object':
            print(f"\n{column} (categorical):")
            print(hospital_data[column].value_counts())
        else:
            print(f"\n{column}:")
            print(f"mean: {hospital_data[column].mean():.2f}")
            print(f"median: {hospital_data[column].median():.2f}")
            print(f"std: {hospital_data[column].std():.2f}")
            print(f"min: {hospital_data[column].min():.2f}")
            print(f"max: {hospital_data[column].max():.2f}")

# histograms for numeric variables
numeric_cols2 = ['Length_of_Stay', 'Num_Medications', 'Num_Diagnoses', 'Readmitted']
for col in numeric_cols2:
    plt.hist(hospital_data[col])
    plt.title(f'{col} distribution')
    plt.xlabel(col)
    plt.ylabel('frequency')
    plt.savefig(f'../graph_pictures/hospital_{col}_histogram.png', dpi=300, bbox_inches='tight')
    plt.close()

# bar charts for categorical variables
plt.bar(hospital_data['Age'].value_counts().index, hospital_data['Age'].value_counts().values)
plt.title('age group distribution')
plt.xticks(rotation=45)
plt.savefig('../graph_pictures/hospital_age_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

plt.bar(hospital_data['Gender'].value_counts().index, hospital_data['Gender'].value_counts().values)
plt.title('gender distribution')
plt.savefig('../graph_pictures/hospital_gender_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

# task 2 - readmission relationships
print("\nTASK 2: readmission relationships")

# readmission by age group
readmit_by_age = hospital_data.groupby('Age')['Readmitted'].mean()
print("readmission rates by age group:")
print(readmit_by_age)

plt.bar(readmit_by_age.index, readmit_by_age.values)
plt.title('readmission rate by age group')
plt.xlabel('age group')
plt.ylabel('readmission rate')
plt.xticks(rotation=45)
plt.savefig('../graph_pictures/readmission_by_age_group.png', dpi=300, bbox_inches='tight')
plt.close()

# readmission by gender
readmit_by_gender = hospital_data.groupby('Gender')['Readmitted'].mean()
print("readmission rates by gender:")
print(readmit_by_gender)

plt.bar(readmit_by_gender.index, readmit_by_gender.values)
plt.title('readmission rate by gender')
plt.xlabel('gender')
plt.ylabel('readmission rate')
plt.savefig('../graph_pictures/readmission_by_gender.png', dpi=300, bbox_inches='tight')
plt.close()

# readmission vs medications
readmitted = hospital_data[hospital_data['Readmitted'] == 1]
not_readmitted = hospital_data[hospital_data['Readmitted'] == 0]

plt.scatter(readmitted['Num_Medications'], readmitted['Readmitted'], label='readmitted', alpha=0.6)
plt.scatter(not_readmitted['Num_Medications'], not_readmitted['Readmitted'], label='not readmitted', alpha=0.6)
plt.title('readmission vs number of medications')
plt.xlabel('number of medications')
plt.ylabel('readmitted (0/1)')
plt.legend()
plt.savefig('../graph_pictures/readmission_vs_medications_scatter.png', dpi=300, bbox_inches='tight')
plt.close()

# boxplot medications by readmission
hospital_data.boxplot(column='Num_Medications', by='Readmitted')
plt.title('medications by readmission status')
plt.savefig('../graph_pictures/medications_by_readmission_boxplot.png', dpi=300, bbox_inches='tight')
plt.close()

print("correlations:")
print(f"medications vs readmission: {hospital_data['Num_Medications'].corr(hospital_data['Readmitted']):.3f}")
print(f"length of stay vs readmission: {hospital_data['Length_of_Stay'].corr(hospital_data['Readmitted']):.3f}")
print(f"diagnoses vs readmission: {hospital_data['Num_Diagnoses'].corr(hospital_data['Readmitted']):.3f}")

# task 3 - age group risk analysis
print("\nTASK 3: age group risk analysis")
print("readmission rates by age group:")
for age_group in hospital_data['Age'].unique():
    group_data = hospital_data[hospital_data['Age'] == age_group]
    readmit_rate = group_data['Readmitted'].mean()
    count = len(group_data)
    print(f"{age_group}: {readmit_rate:.3f} ({count} patients)")

highest_risk = readmit_by_age.idxmax()
highest_rate = readmit_by_age.max()
print(f"highest risk group: {highest_risk} with rate {highest_rate:.3f}")