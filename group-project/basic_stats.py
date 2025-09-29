import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 8)
plt.rcParams['font.size'] = 10

# Load the data
df = pd.read_csv('CSVS/Death_rates_for_suicide__by_sex__race__Hispanic_origin__and_age__United_States.csv')

# Create markdown output
markdown_output = []

# Header
markdown_output.append("# 📊 Suicide Death Rates Analysis")
markdown_output.append("## United States, 1950-2018")
markdown_output.append(f"\n*Analysis generated: {datetime.now().strftime('%B %d, %Y')}*")
markdown_output.append("\n---\n")

# Table of Contents
markdown_output.append("## 📑 Table of Contents")
markdown_output.append("1. [Dataset Source and Methodology](#dataset-source-and-methodology)")
markdown_output.append("2. [Dataset Overview](#dataset-overview)")
markdown_output.append("3. [Data Quality Check](#data-quality-check)")
markdown_output.append("4. [Key Statistics](#key-statistics)")
markdown_output.append("5. [Demographic Categories](#demographic-categories)")
markdown_output.append("6. [Age Group Distribution](#age-group-distribution)")
markdown_output.append("7. [Temporal Coverage](#temporal-coverage)")
markdown_output.append("8. [Visualizations](#visualizations)")
markdown_output.append("9. [Summary of Key Findings](#summary-of-key-findings)")
markdown_output.append("10. [Resources](#resources)")
markdown_output.append("\n---\n")

# Section 1: Dataset Source
markdown_output.append("## 📚 Dataset Source and Methodology")
markdown_output.append("\n### 📄 Official Description")
markdown_output.append("Data on death rates for suicide, by selected population characteristics. Please refer to the PDF or Excel version of this table in the HUS 2019 Data Finder for critical information about measures, definitions, and changes over time.")
markdown_output.append("\n🔗 **[HUS 2019 Data Finder](https://www.cdc.gov/nchs/hus/contents2019.htm)**")

markdown_output.append("\n### 📊 Data Sources")
markdown_output.append("- National Center for Health Statistics (NCHS)")
markdown_output.append("- National Vital Statistics System (NVSS)")
markdown_output.append("- U.S. Census Bureau national population estimates")

markdown_output.append("\n### 📖 Key References")
markdown_output.append("1. **Grove RD, Hetzel AM.** *Vital statistics rates in the United States, 1940–1960.* National Center for Health Statistics. 1968")
markdown_output.append("\n2. **Murphy SL, Xu JQ, Kochanek KD, Arias E, Tejada-Vera B.** *Deaths: Final data for 2018.* National Vital Statistics Reports; vol 69 no 13. Hyattsville, MD: NCHS. 2021")
markdown_output.append("   - 🔗 [Available here](https://www.cdc.gov/nchs/products/nvsr.htm)")

markdown_output.append("\n### 📋 Methodology")
markdown_output.append("| Component | Description |")
markdown_output.append("|-----------|-------------|")
markdown_output.append("| **Numerator** | NVSS annual public-use Mortality Files |")
markdown_output.append("| **Denominator** | U.S. Census Bureau national population estimates |")
markdown_output.append("| **Rate Format** | Deaths per 100,000 resident population |")
markdown_output.append("| **Adjustment** | Age-adjusted to allow fair demographic comparisons |")

markdown_output.append("\n> ⚠️ **Important Notes:**")
markdown_output.append("> - Definitions and measurement methods may have changed over time")
markdown_output.append("> - Refer to official documentation for critical details about changes")
markdown_output.append("> - [Appendix information](https://www.cdc.gov/nchs/data/hus/hus19-appendix-508.pdf)")
markdown_output.append("> - This analysis is for educational/research purposes")

markdown_output.append("\n---\n")

# Section 2: Dataset Overview
markdown_output.append("## 📊 Dataset Overview")
markdown_output.append("\n### What This Dataset Contains")
markdown_output.append("This is a comprehensive dataset from the CDC tracking suicide death rates across different demographics in the United States. Rates are standardized per 100,000 population to allow fair comparisons across groups.")

markdown_output.append(f"\n### Quick Facts")
markdown_output.append("| Metric | Value |")
markdown_output.append("|--------|-------|")
markdown_output.append(f"| **Dataset Dimensions** | {df.shape[0]:,} rows × {df.shape[1]} columns |")
markdown_output.append(f"| **Time Period** | {df['YEAR'].min()} - {df['YEAR'].max()} ({df['YEAR'].max() - df['YEAR'].min() + 1} years) |")
markdown_output.append(f"| **Memory Usage** | {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB |")

markdown_output.append("\n### 💡 Why This Matters")
markdown_output.append("Understanding suicide rates across different populations helps identify at-risk groups and informs prevention strategies and mental health policies.")

markdown_output.append("\n---\n")

# Section 3: Data Quality
markdown_output.append("## 🔍 Data Quality Check")
markdown_output.append("\n### Understanding Missing Data")
markdown_output.append("Missing data can occur when:")
markdown_output.append("- ✓ Sample sizes are too small to report reliably (statistical reliability)")
markdown_output.append("- ✓ Data wasn't collected for certain demographics in earlier years")
markdown_output.append("- ✓ Privacy protections suppress data to prevent identification")
markdown_output.append("- ✓ Methodological changes over time affect data availability")

missing_data = df.isnull().sum()
missing_pct = (missing_data / len(df) * 100).round(2)
quality_df = pd.DataFrame({
    'Missing Count': missing_data,
    'Missing %': missing_pct
}).sort_values('Missing Count', ascending=False)

markdown_output.append("\n### Missing Data Summary")
markdown_output.append("| Column | Missing Count | Missing % |")
markdown_output.append("|--------|---------------|-----------|")
for col, row in quality_df[quality_df['Missing Count'] > 0].iterrows():
    markdown_output.append(f"| **{col}** | {int(row['Missing Count']):,} | {row['Missing %']:.2f}% |")

complete_records = df['ESTIMATE'].notna().sum()
complete_pct = (complete_records/len(df)*100)
markdown_output.append(f"\n✅ **Complete records with ESTIMATE values:** {complete_records:,} ({complete_pct:.1f}%)")

markdown_output.append("\n### 💡 Interpretation")
markdown_output.append("- FLAG column is mostly empty (normal - only marks special cases)")
markdown_output.append(f"- ESTIMATE has {missing_data['ESTIMATE']} missing values ({missing_pct['ESTIMATE']:.1f}%)")
markdown_output.append("- This level of completeness is excellent for epidemiological data")
markdown_output.append("- Missing estimates often indicate unreliable data due to small sample sizes")

markdown_output.append("\n---\n")

# Section 4: Key Statistics
markdown_output.append("## 📈 Key Statistics")
markdown_output.append("### Suicide Death Rate Statistics (per 100,000 population)")

markdown_output.append("\n#### What These Numbers Mean")
markdown_output.append("Rates are expressed per 100,000 people, making it easier to compare groups of different sizes. For example, a rate of 13.7 means about 13.7 deaths per 100,000 people in that demographic group. This standardization follows NCHS methodology for vital statistics.")

stats_df = df['ESTIMATE'].describe()

markdown_output.append("\n### Statistical Summary")
markdown_output.append("| Statistic | Value | Interpretation |")
markdown_output.append("|-----------|-------|----------------|")
markdown_output.append(f"| **Mean Rate** | {stats_df['mean']:.2f} | Average across all groups and years |")
markdown_output.append(f"| **Median Rate** | {stats_df['50%']:.2f} | Middle value - less affected by extremes |")
markdown_output.append(f"| **Std Deviation** | {stats_df['std']:.2f} | Measure of variability |")
markdown_output.append(f"| **Min Rate** | {stats_df['min']:.2f} | Lowest recorded rate |")
markdown_output.append(f"| **Max Rate** | {stats_df['max']:.2f} | Highest recorded rate |")
markdown_output.append(f"| **25th Percentile** | {stats_df['25%']:.2f} | 25% of rates are below this |")
markdown_output.append(f"| **75th Percentile** | {stats_df['75%']:.2f} | 75% of rates are below this |")

markdown_output.append("\n### 💡 Key Insights")
markdown_output.append(f"1. **Distribution Shape:** The mean ({stats_df['mean']:.2f}) is higher than median ({stats_df['50%']:.2f}), indicating a right-skewed distribution (some very high rates pull the average up)")
markdown_output.append(f"2. **Variability:** High standard deviation ({stats_df['std']:.2f}) shows substantial variation across different demographics and time periods")
markdown_output.append(f"3. **Range:** The range from {stats_df['min']:.2f} to {stats_df['max']:.2f} demonstrates dramatic differences between lowest and highest risk groups")

markdown_output.append("\n---\n")

# Section 5: Demographics
markdown_output.append("## 👥 Demographic Categories")
markdown_output.append("\n### How the Data is Organized")
markdown_output.append("The dataset breaks down suicide rates by multiple demographic factors following NCHS population classification standards. This allows researchers to identify patterns and health disparities.")

markdown_output.append("\n### Available Breakdowns")
markdown_output.append("| # | Category | Record Count |")
markdown_output.append("|---|----------|--------------|")
for i, stub in enumerate(df['STUB_NAME'].unique(), 1):
    count = (df['STUB_NAME'] == stub).sum()
    markdown_output.append(f"| {i} | {stub} | {count:,} |")

markdown_output.append("\n### 💡 What These Categories Tell Us")
markdown_output.append("- **Total:** Overall population rates (age-adjusted)")
markdown_output.append("- **Sex:** Differences between males and females")
markdown_output.append("- **Sex and race:** Intersection of gender and racial identity")
markdown_output.append("- **Age:** How rates vary across different age groups")
markdown_output.append("- **Combined categories:** More detailed demographic intersections")
markdown_output.append("- **Single race:** Individuals identifying with one race only")
markdown_output.append("  - *Note: Classification methods changed in 1997 with new OMB standards*")
markdown_output.append("\n> More specific breakdowns help identify which groups face the highest risk")

markdown_output.append("\n---\n")

# Section 6: Age Groups
markdown_output.append("## 🎂 Age Group Distribution")
markdown_output.append("\n### Why Age Matters")
markdown_output.append("Suicide risk varies significantly across the lifespan. Understanding age-specific patterns helps target prevention efforts effectively. Age-adjusted rates account for differences in population age structure.")

age_groups = sorted(df['AGE'].unique())
markdown_output.append(f"\n**Total Age Categories:** {len(age_groups)}")
markdown_output.append("\n### Age Categories")
for i, age in enumerate(age_groups, 1):
    markdown_output.append(f"{i}. {age}")

markdown_output.append("\n### 💡 Age-Related Insights")
markdown_output.append("- **Youth and young adults** often face unique risk factors (bullying, identity issues)")
markdown_output.append("- **Middle-aged adults** may experience work/financial stress")
markdown_output.append("- **Older adults** can face isolation, health issues, and loss")
markdown_output.append("- **Age-adjusted rates** use standard population to allow fair comparisons")
markdown_output.append("- Different age categorizations may be used across time periods")

markdown_output.append("\n---\n")

# Section 7: Temporal Coverage
markdown_output.append("## 📅 Temporal Coverage")
markdown_output.append("\n### Examining Trends Over Time")
markdown_output.append("Looking at how suicide rates change over decades reveals the impact of societal changes, economic conditions, policy interventions, and improvements (or gaps) in mental health care.")
markdown_output.append("\n> ⚠️ **Note:** Definitions and collection methods may have changed over this time period. Consult official documentation for specifics.")

year_counts = df.groupby('YEAR').size()
markdown_output.append(f"\n**Records per year range:** {year_counts.min()} - {year_counts.max()}")
markdown_output.append(f"\n**Average records per year:** {year_counts.mean():.0f}")

df['DECADE'] = (df['YEAR'] // 10) * 10
decade_summary = df.groupby('DECADE').agg({
    'ESTIMATE': ['count', 'mean', 'std']
}).round(2)
decade_summary.columns = ['Record Count', 'Average Rate', 'Std Deviation']

markdown_output.append("\n### Summary by Decade")
markdown_output.append("| Decade | Record Count | Average Rate | Std Deviation |")
markdown_output.append("|--------|--------------|--------------|---------------|")
for decade, row in decade_summary.iterrows():
    markdown_output.append(f"| {int(decade)}s | {int(row['Record Count']):,} | {row['Average Rate']:.2f} | {row['Std Deviation']:.2f} |")

recent_decades = df[df['YEAR'] >= 1990].groupby('DECADE')['ESTIMATE'].mean()
if len(recent_decades) > 1:
    trend = "📉 decreasing" if recent_decades.iloc[-1] < recent_decades.iloc[0] else "📈 increasing"
    markdown_output.append(f"\n### 💡 Temporal Patterns")
    markdown_output.append(f"- **Overall trend since 1990:** {trend}")

markdown_output.append("- More recent years have more detailed demographic breakdowns")
markdown_output.append("- Earlier decades may have less granular data due to collection methods")
markdown_output.append("- Spikes or drops may reflect major societal events or policy changes")
markdown_output.append("- **1997** saw changes in racial classification standards (OMB standards)")
markdown_output.append("- Always consider methodological changes when comparing across decades")

markdown_output.append("\n---\n")

# Generate visualizations
print("📊 Generating visualizations...")

fig = plt.figure(figsize=(16, 10))
fig.suptitle('Suicide Death Rates in the United States - Statistical Overview\nData Source: NCHS National Vital Statistics System', 
             fontsize=15, fontweight='bold', y=0.997)

# 1. Distribution
ax1 = plt.subplot(2, 3, 1)
df['ESTIMATE'].dropna().hist(bins=50, edgecolor='black', alpha=0.7, color='steelblue')
ax1.set_xlabel('Death Rate (per 100,000)')
ax1.set_ylabel('Frequency')
ax1.set_title('Distribution of Death Rates')
ax1.axvline(df['ESTIMATE'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {df["ESTIMATE"].mean():.2f}')
ax1.axvline(df['ESTIMATE'].median(), color='green', linestyle='--', linewidth=2, label=f'Median: {df["ESTIMATE"].median():.2f}')
ax1.legend()

# 2. Trend over time
ax2 = plt.subplot(2, 3, 2)
yearly_avg = df.groupby('YEAR')['ESTIMATE'].mean()
ax2.plot(yearly_avg.index, yearly_avg.values, linewidth=2, color='darkblue', marker='o', markersize=4)
ax2.set_xlabel('Year')
ax2.set_ylabel('Average Death Rate')
ax2.set_title('Average Suicide Death Rate Over Time')
ax2.grid(True, alpha=0.3)
ax2.axvline(1997, color='orange', linestyle=':', linewidth=1.5, alpha=0.7, label='1997: Classification change')
ax2.legend(fontsize=8)

# 3. Box plot by decade
ax3 = plt.subplot(2, 3, 3)
df_decade = df[df['ESTIMATE'].notna()].copy()
sns.boxplot(data=df_decade, x='DECADE', y='ESTIMATE', hue='DECADE', palette='Blues', ax=ax3, legend=False)
ax3.set_xlabel('Decade')
ax3.set_ylabel('Death Rate')
ax3.set_title('Death Rate Distribution by Decade')
ax3.tick_params(axis='x', rotation=45)

# 4. Records per year
ax4 = plt.subplot(2, 3, 4)
year_counts.plot(kind='bar', color='teal', alpha=0.7, ax=ax4)
ax4.set_xlabel('Year')
ax4.set_ylabel('Number of Records')
ax4.set_title('Data Availability by Year')
ax4.tick_params(axis='x', rotation=45, labelsize=7)

# 5. Top 10 highest rates
ax5 = plt.subplot(2, 3, 5)
top_rates = df.nlargest(10, 'ESTIMATE')[['STUB_LABEL', 'YEAR', 'ESTIMATE', 'AGE']]
colors = plt.cm.Reds(np.linspace(0.4, 0.9, 10))
ax5.barh(range(10), top_rates['ESTIMATE'].values, color=colors)
ax5.set_yticks(range(10))
ax5.set_yticklabels([f"{row['STUB_LABEL'][:25]}... ({row['YEAR']})" for _, row in top_rates.iterrows()], fontsize=8)
ax5.set_xlabel('Death Rate (per 100,000)')
ax5.set_title('Top 10 Highest Death Rates')
ax5.invert_yaxis()

# 6. Missing data
ax6 = plt.subplot(2, 3, 6)
missing_cols = quality_df[quality_df['Missing Count'] > 0]['Missing %']
if len(missing_cols) > 0:
    missing_cols.plot(kind='barh', color='coral', ax=ax6)
    ax6.set_xlabel('Missing Data (%)')
    ax6.set_title('Missing Data by Column')
else:
    ax6.text(0.5, 0.5, 'No Missing Data!', ha='center', va='center', fontsize=14, color='green', weight='bold')
    ax6.axis('off')

plt.tight_layout()
plt.savefig('suicide_stats_overview.png', dpi=300, bbox_inches='tight')
print("✓ Saved: suicide_stats_overview.png")

# Section 8: Visualizations
markdown_output.append("## 📊 Visualizations")
markdown_output.append("\n![Statistical Overview](suicide_stats_overview.png)")
markdown_output.append("\n*Figure: Comprehensive statistical overview including distribution, temporal trends, and demographic patterns*")

markdown_output.append("\n---\n")

# Section 9: Summary
markdown_output.append("## 📋 Summary of Key Findings")
markdown_output.append("\n### 🔍 What We Learned")
markdown_output.append(f"1. The dataset spans **{df['YEAR'].max() - df['YEAR'].min() + 1} years** of suicide mortality data")
markdown_output.append(f"2. Average death rate is **{df['ESTIMATE'].mean():.2f}** per 100,000 population")
markdown_output.append(f"3. Rates vary dramatically (from **{df['ESTIMATE'].min():.2f}** to **{df['ESTIMATE'].max():.2f}**)")
markdown_output.append(f"4. Data includes **{len(df['STUB_NAME'].unique())}** different demographic breakdowns")
markdown_output.append(f"5. **{(df['ESTIMATE'].notna().sum()/len(df)*100):.1f}%** of records have complete rate data")

markdown_output.append("\n### 📊 Next Steps for Deeper Analysis")
markdown_output.append("- Compare rates between males and females")
markdown_output.append("- Analyze racial and ethnic disparities")
markdown_output.append("- Examine age-specific trends over time")
markdown_output.append("- Investigate correlations with historical events")
markdown_output.append("- Perform statistical tests for significant differences between groups")
markdown_output.append("- Create predictive models for future trends")
markdown_output.append("- Account for methodological changes when making longitudinal comparisons")

markdown_output.append("\n### ⚠️ Important Considerations")
markdown_output.append("- These are rates, not absolute numbers - consider population sizes")
markdown_output.append("- Missing data may indicate unreliable estimates for small populations")
markdown_output.append("- Correlation does not imply causation")
markdown_output.append("- Cultural and reporting differences may affect cross-group comparisons")
markdown_output.append("- Always consider the broader context of mental health and social factors")
markdown_output.append("- Definitions and methods may have changed over the 68-year span")
markdown_output.append("- Consult official CDC documentation for methodological details")

markdown_output.append("\n---\n")

# Data Citation
markdown_output.append("## 📚 Data Citation")
markdown_output.append("\n> National Center for Health Statistics (NCHS). National Vital Statistics System (NVSS). Death rates for suicide by selected population characteristics, United States, 1950-2018. *Health, United States, 2019*. Available from: https://www.cdc.gov/nchs/hus/contents2019.htm")

markdown_output.append("\n---\n")

# Section 10: Resources
markdown_output.append("## 💚 Resources")
markdown_output.append("\n### If You or Someone You Know is Struggling")
markdown_output.append("- **National Suicide Prevention Lifeline:** 988")
markdown_output.append("- **Crisis Text Line:** Text HOME to 741741")
markdown_output.append("- **International Association for Suicide Prevention:** https://www.iasp.info")

markdown_output.append("\n### For More Information About This Data")
markdown_output.append("- **CDC NCHS:** https://www.cdc.gov/nchs/")
markdown_output.append("- **NVSS:** https://www.cdc.gov/nchs/nvss/")
markdown_output.append("- **HUS 2019 Appendix:** https://www.cdc.gov/nchs/data/hus/hus19-appendix-508.pdf")

markdown_output.append("\n---\n")
markdown_output.append(f"\n*Analysis completed: {datetime.now().strftime('%B %d, %Y at %I:%M %p')}*")

# Write to file
with open('suicide_stats_analysis.md', 'w') as f:
    f.write('\n'.join(markdown_output))

print("✓ Saved: suicide_stats_analysis.md")
print("\n" + "="*80)
print("✓ ANALYSIS COMPLETE!")
print("="*80)
print("\nGenerated files:")
print("  📄 suicide_stats_analysis.md - Markdown report")
print("  📊 suicide_stats_overview.png - Visualizations")