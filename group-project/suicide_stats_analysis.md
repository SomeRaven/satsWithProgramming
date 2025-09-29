# 📊 Suicide Death Rates Analysis
## United States, 1950-2018

*Analysis generated: September 29, 2025*

---

## 📑 Table of Contents
1. [Dataset Source and Methodology](#dataset-source-and-methodology)
2. [Dataset Overview](#dataset-overview)
3. [Data Quality Check](#data-quality-check)
4. [Key Statistics](#key-statistics)
5. [Demographic Categories](#demographic-categories)
6. [Age Group Distribution](#age-group-distribution)
7. [Temporal Coverage](#temporal-coverage)
8. [Visualizations](#visualizations)
9. [Summary of Key Findings](#summary-of-key-findings)
10. [Resources](#resources)

---

## 📚 Dataset Source and Methodology

### 📄 Official Description
Data on death rates for suicide, by selected population characteristics. Please refer to the PDF or Excel version of this table in the HUS 2019 Data Finder for critical information about measures, definitions, and changes over time.

🔗 **[HUS 2019 Data Finder](https://www.cdc.gov/nchs/hus/contents2019.htm)**

### 📊 Data Sources
- National Center for Health Statistics (NCHS)
- National Vital Statistics System (NVSS)
- U.S. Census Bureau national population estimates

### 📖 Key References
1. **Grove RD, Hetzel AM.** *Vital statistics rates in the United States, 1940–1960.* National Center for Health Statistics. 1968

2. **Murphy SL, Xu JQ, Kochanek KD, Arias E, Tejada-Vera B.** *Deaths: Final data for 2018.* National Vital Statistics Reports; vol 69 no 13. Hyattsville, MD: NCHS. 2021
   - 🔗 [Available here](https://www.cdc.gov/nchs/products/nvsr.htm)

### 📋 Methodology
| Component | Description |
|-----------|-------------|
| **Numerator** | NVSS annual public-use Mortality Files |
| **Denominator** | U.S. Census Bureau national population estimates |
| **Rate Format** | Deaths per 100,000 resident population |
| **Adjustment** | Age-adjusted to allow fair demographic comparisons |

> ⚠️ **Important Notes:**
> - Definitions and measurement methods may have changed over time
> - Refer to official documentation for critical details about changes
> - [Appendix information](https://www.cdc.gov/nchs/data/hus/hus19-appendix-508.pdf)
> - This analysis is for educational/research purposes

---

## 📊 Dataset Overview

### What This Dataset Contains
This is a comprehensive dataset from the CDC tracking suicide death rates across different demographics in the United States. Rates are standardized per 100,000 population to allow fair comparisons across groups.

### Quick Facts
| Metric | Value |
|--------|-------|
| **Dataset Dimensions** | 6,390 rows × 13 columns |
| **Time Period** | 1950 - 2018 (69 years) |
| **Memory Usage** | 2.88 MB |

### 💡 Why This Matters
Understanding suicide rates across different populations helps identify at-risk groups and informs prevention strategies and mental health policies.

---

## 🔍 Data Quality Check

### Understanding Missing Data
Missing data can occur when:
- ✓ Sample sizes are too small to report reliably (statistical reliability)
- ✓ Data wasn't collected for certain demographics in earlier years
- ✓ Privacy protections suppress data to prevent identification
- ✓ Methodological changes over time affect data availability

### Missing Data Summary
| Column | Missing Count | Missing % |
|--------|---------------|-----------|
| **FLAG** | 5,484 | 85.82% |
| **ESTIMATE** | 906 | 14.18% |

✅ **Complete records with ESTIMATE values:** 5,484 (85.8%)

### 💡 Interpretation
- FLAG column is mostly empty (normal - only marks special cases)
- ESTIMATE has 906 missing values (14.2%)
- This level of completeness is excellent for epidemiological data
- Missing estimates often indicate unreliable data due to small sample sizes

---

## 📈 Key Statistics
### Suicide Death Rate Statistics (per 100,000 population)

#### What These Numbers Mean
Rates are expressed per 100,000 people, making it easier to compare groups of different sizes. For example, a rate of 13.7 means about 13.7 deaths per 100,000 people in that demographic group. This standardization follows NCHS methodology for vital statistics.

### Statistical Summary
| Statistic | Value | Interpretation |
|-----------|-------|----------------|
| **Mean Rate** | 13.71 | Average across all groups and years |
| **Median Rate** | 10.50 | Middle value - less affected by extremes |
| **Std Deviation** | 11.53 | Measure of variability |
| **Min Rate** | 0.30 | Lowest recorded rate |
| **Max Rate** | 74.80 | Highest recorded rate |
| **25th Percentile** | 5.00 | 25% of rates are below this |
| **75th Percentile** | 19.50 | 75% of rates are below this |

### 💡 Key Insights
1. **Distribution Shape:** The mean (13.71) is higher than median (10.50), indicating a right-skewed distribution (some very high rates pull the average up)
2. **Variability:** High standard deviation (11.53) shows substantial variation across different demographics and time periods
3. **Range:** The range from 0.30 to 74.80 demonstrates dramatic differences between lowest and highest risk groups

---

## 👥 Demographic Categories

### How the Data is Organized
The dataset breaks down suicide rates by multiple demographic factors following NCHS population classification standards. This allows researchers to identify patterns and health disparities.

### Available Breakdowns
| # | Category | Record Count |
|---|----------|--------------|
| 1 | Total | 84 |
| 2 | Sex | 168 |
| 3 | Sex and race | 672 |
| 4 | Sex and race and Hispanic origin | 664 |
| 5 | Sex and race (Single race) | 12 |
| 6 | Sex and race and Hispanic origin (Single race) | 24 |
| 7 | Age | 588 |
| 8 | Sex and age | 1,176 |
| 9 | Sex, age and race | 1,596 |
| 10 | Sex, age and race and Hispanic origin | 1,328 |
| 11 | Sex, age and race (Single race) | 30 |
| 12 | Sex, age and race and Hispanic origin (Single race) | 48 |

### 💡 What These Categories Tell Us
- **Total:** Overall population rates (age-adjusted)
- **Sex:** Differences between males and females
- **Sex and race:** Intersection of gender and racial identity
- **Age:** How rates vary across different age groups
- **Combined categories:** More detailed demographic intersections
- **Single race:** Individuals identifying with one race only
  - *Note: Classification methods changed in 1997 with new OMB standards*

> More specific breakdowns help identify which groups face the highest risk

---

## 🎂 Age Group Distribution

### Why Age Matters
Suicide risk varies significantly across the lifespan. Understanding age-specific patterns helps target prevention efforts effectively. Age-adjusted rates account for differences in population age structure.

**Total Age Categories:** 15

### Age Categories
1. 10-14 years
2. 15-19 years
3. 15-24 years
4. 20-24 years
5. 25-34 years
6. 25-44 years
7. 35-44 years
8. 45-54 years
9. 45-64 years
10. 55-64 years
11. 65 years and over
12. 65-74 years
13. 75-84 years
14. 85 years and over
15. All ages

### 💡 Age-Related Insights
- **Youth and young adults** often face unique risk factors (bullying, identity issues)
- **Middle-aged adults** may experience work/financial stress
- **Older adults** can face isolation, health issues, and loss
- **Age-adjusted rates** use standard population to allow fair comparisons
- Different age categorizations may be used across time periods

---

## 📅 Temporal Coverage

### Examining Trends Over Time
Looking at how suicide rates change over decades reveals the impact of societal changes, economic conditions, policy interventions, and improvements (or gaps) in mental health care.

> ⚠️ **Note:** Definitions and collection methods may have changed over this time period. Consult official documentation for specifics.

**Records per year range:** 138 - 276

**Average records per year:** 152

### Summary by Decade
| Decade | Record Count | Average Rate | Std Deviation |
|--------|--------------|--------------|---------------|
| 1950s | 74 | 17.02 | 16.97 |
| 1960s | 73 | 16.17 | 14.88 |
| 1970s | 76 | 15.54 | 11.54 |
| 1980s | 978 | 15.37 | 12.65 |
| 1990s | 1,234 | 13.97 | 12.09 |
| 2000s | 1,537 | 11.92 | 9.92 |
| 2010s | 1,512 | 13.87 | 11.07 |

### 💡 Temporal Patterns
- **Overall trend since 1990:** 📉 decreasing
- More recent years have more detailed demographic breakdowns
- Earlier decades may have less granular data due to collection methods
- Spikes or drops may reflect major societal events or policy changes
- **1997** saw changes in racial classification standards (OMB standards)
- Always consider methodological changes when comparing across decades

---

## 📊 Visualizations

![Statistical Overview](suicide_stats_overview.png)

*Figure: Comprehensive statistical overview including distribution, temporal trends, and demographic patterns*

---

## 📋 Summary of Key Findings

### 🔍 What We Learned
1. The dataset spans **69 years** of suicide mortality data
2. Average death rate is **13.71** per 100,000 population
3. Rates vary dramatically (from **0.30** to **74.80**)
4. Data includes **12** different demographic breakdowns
5. **85.8%** of records have complete rate data

### 📊 Next Steps for Deeper Analysis
- Compare rates between males and females
- Analyze racial and ethnic disparities
- Examine age-specific trends over time
- Investigate correlations with historical events
- Perform statistical tests for significant differences between groups
- Create predictive models for future trends
- Account for methodological changes when making longitudinal comparisons

### ⚠️ Important Considerations
- These are rates, not absolute numbers - consider population sizes
- Missing data may indicate unreliable estimates for small populations
- Correlation does not imply causation
- Cultural and reporting differences may affect cross-group comparisons
- Always consider the broader context of mental health and social factors
- Definitions and methods may have changed over the 68-year span
- Consult official CDC documentation for methodological details

---

## 📚 Data Citation

> National Center for Health Statistics (NCHS). National Vital Statistics System (NVSS). Death rates for suicide by selected population characteristics, United States, 1950-2018. *Health, United States, 2019*. Available from: https://www.cdc.gov/nchs/hus/contents2019.htm

---

## 💚 Resources

### If You or Someone You Know is Struggling
- **National Suicide Prevention Lifeline:** 988
- **Crisis Text Line:** Text HOME to 741741
- **International Association for Suicide Prevention:** https://www.iasp.info

### For More Information About This Data
- **CDC NCHS:** https://www.cdc.gov/nchs/
- **NVSS:** https://www.cdc.gov/nchs/nvss/
- **HUS 2019 Appendix:** https://www.cdc.gov/nchs/data/hus/hus19-appendix-508.pdf

---


*Analysis completed: September 29, 2025 at 02:28 PM*