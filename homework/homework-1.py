import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Color class for easy formatting
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

# Extract Data from csvs
athlete = pd.read_csv("CSVS/athlete_wearable_dataset.csv")
tech = pd.read_csv("CSVS/tech_salaries_dataset.csv")

#Athlete Data breakdown 
print("\n" + "="*80)
print(C.BOLD + C.BLUE + "🏃 ATHLETE DATASET INFORMATION 🏃" + C.END)
print("="*80 + "\n")

print(C.BOLD + C.GREEN + "📊 HEAD:" + C.END)
print(athlete.head())
print("\n" + "-"*80 + "\n")

print(C.BOLD + C.GREEN + "ℹ️  INFO:" + C.END)
athlete.info()
print("\n" + "-"*80 + "\n")

print(C.BOLD + C.GREEN + "📈 DESCRIBE:" + C.END)
print(athlete.describe())
print("\n" + "-"*80 + "\n")

print(C.BOLD + C.YELLOW + "⚠️  NULL VALUES:" + C.END)
print(athlete.isnull().sum())
print("\n" + "-"*80 + "\n")

print(C.BOLD + C.PURPLE + "🔍 UNIQUE VALUES:" + C.END)
print(athlete.value_counts())
print("\n" + "-"*80 + "\n")

# for loop to print each column but prettier to look at :D
print(C.BOLD + C.PURPLE + "📊 Variable Names:" + C.END)
print()
for column in athlete.columns:
    print(f"⚫️ {column}")
print("\n" + "-"*80 + "\n")


# Tech Data Breakdown 
print("\n" + "="*80)
print(C.BOLD + C.BLUE + "💻 TECH DATASET INFORMATION 💻" + C.END)
print("="*80 + "\n")

print(C.BOLD + C.GREEN + "📊 HEAD:" + C.END)
print(tech.head())
print("\n" + "-"*80 + "\n")

print(C.BOLD + C.GREEN + "ℹ️  INFO:" + C.END)
print(tech.info())
print("="*80 + "\n")

print(C.BOLD + C.GREEN + "📈 DESCRIBE:" + C.END)
print(tech.describe())
print("="*80 + "\n")

print(C.BOLD + C.YELLOW + "⚠️  NULL VALUES:" + C.END)
print(tech.isnull().sum())
print("="*80 + "\n")

print(C.BOLD + C.PURPLE + "🔍 UNIQUE VALUES:" + C.END)
print(tech.value_counts())
print("="*80 + "\n")

# for loop to print each column but prettier to look at :D

print(C.BOLD + C.PURPLE + "📊 Variable Names:" + C.END)
print()
for column in tech.columns:
    print(f"⚫️ {column}")
print("\n" + "-"*80 + "\n")


# Start of Case Study 1 (Tech)
print("\n" + "="*80)
print(C.BOLD + C.BLUE + "💻 ACTUAL CASE STUDY 1 💻" + C.END)
print("="*80 + "\n")

# total job counts
print(C.BLUE +"📊 Job Title counts:" + C.END)
print(tech['JobTitle'].value_counts())
print()

# total of languages used 
print(C.BLUE + "📊 Primary Language counts:" + C.END)
print(tech['PrimaryLanguage'].value_counts())

# pie chart for primary languages 

# language_counts = tech["PrimaryLanguage"].value_counts()
# plt.pie(language_counts.values, labels=language_counts.index, autopct="%.1f%%")
# plt.title("Programming Language Distribution")
# plt.show()

# pie chart for jobs distribution 

# job_counts = tech["JobTitle"].value_counts()
# plt.pie(job_counts.values, labels=job_counts.index, autopct="%.1f%%")
# plt.title("Job Title Distribution")
# plt.show()

# start of tech salaries 
salaries = tech["Salary"]

# histagram for salaries per job
# plt.hist(tech["Salary"])
# plt.title("Salaries Per Job")
# plt.show()


print("Salary Mean: ")
sal_mean = salaries.mean()
print(sal_mean)

print("Salary Median: ")
sal_med = salaries.median()
print(sal_med)

'''
    For Salary data
    If the skew is greater than 0.5 then salary is right-skewed
    If the skew is less then -0.5 then salary is left-skewed
    If neither then salary is symmetric
'''
salary_skew = tech['Salary'].skew()
print(f"Salary skewness: {salary_skew:.2f}")

if salary_skew > 0.5:
    print(f"{C.BOLD}{C.YELLOW}RIGHT-SKEWED: Few people earn very high salaries{C.END}")
elif salary_skew < -0.5:
    print(f"{C.BOLD}{C.YELLOW}LEFT-SKEWED: Few people earn very low salaries{C.END}")
else:
    print(f"{C.BOLD}{C.GREEN}SYMMETRIC: Salaries are evenly distributed{C.END}")

print(f"{C.BOLD}Mean: ${sal_mean:,.0f}, Median: ${sal_med:,.0f}{C.END}")

'''
    start of Salary vs Experience
    Scatterplot with x = experience and y = salary 
'''
plt.figure(figsize=(10, 6))
sns.scatterplot(x="YearsExperience", y="Salary", data=tech, alpha=0.6)
sns.regplot(x="YearsExperience", y="Salary", data=tech, scatter=False, color='red')

plt.xlabel("Years of Experience")
plt.ylabel("Salary ($)")
plt.title("Salary vs Experience Relationship")
plt.show()

correlation = tech["YearsExperience"].corr(tech["Salary"])
print(f"Correlation between Experience and Salary: {correlation:.3f}")

# Languages by Experience

binsX = [0 , 2, 5, 10, float('inf')]
lablesX = ['Junior (0-2)', 'Mid (3-5)', 'Senior (6-10)', 'Expert (11+)']

tech['ExperienceGroup'] = pd.cut(tech["YearsExperience"],
                                      bins=binsX,
                                      labels=lablesX)

print("Experience groups created!")
print(tech['ExperienceGroup'].value_counts())

# Find average salaries for each language and experience combination
salary_by_lang_exp = tech.groupby(['ExperienceGroup', 'PrimaryLanguage'])['Salary'].mean().unstack()

# Create bar chart to show the lang salary diff. 
plt.figure(figsize=(12, 8))
salary_by_lang_exp.plot(kind='bar', ax=plt.gca(), width=0.8)
plt.title('Average Salary by Experience Group and Programming Language', fontsize=16, fontweight='bold')
plt.xlabel('Experience Group', fontweight='bold')
plt.ylabel('Average Salary ($)', fontweight='bold')
plt.xticks(rotation=45)
plt.legend(title='Programming Language', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Add this after your bar chart:
plt.figure(figsize=(15, 8))
sns.boxplot(data=tech, x='PrimaryLanguage', y='Salary', hue='ExperienceGroup')
plt.title('Salary by Programming Language and Experience Level')
plt.xlabel('Programming Language')
plt.ylabel('Salary ($)')
plt.xticks(rotation=45)
plt.legend(title='Experience Level', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Add this to find which language pays best at each level:
print(C.BOLD + C.GREEN + "\n🏆 Highest paying languages by experience:" + C.END)
for exp_group in lablesX:
    group_data = tech[tech['ExperienceGroup'] == exp_group]
    if len(group_data) > 0:
        lang_averages = group_data.groupby('PrimaryLanguage')['Salary'].mean().sort_values(ascending=False)
        highest_lang = lang_averages.index[0]
        highest_salary = lang_averages.iloc[0]
        print(f"• {exp_group}: {highest_lang} (${highest_salary:,.0f})")