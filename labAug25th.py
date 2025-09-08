"""
================================================================================
LAB NOTES: Random Sampling & Data Visualization with Pandas
Course: Applied Statistics with Programming
Date: August 25, 2025
Topic: Random sampling methods, data cleaning, and multiple visualization types
================================================================================
"""

import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for better-looking plots
plt.style.use('default')
sns.set_palette("husl")

print("=" * 80)
print("🎲 PART 1: RANDOM SAMPLING METHODS")
print("=" * 80)

# Sample data to work with
list1 = [1, 2, 3, 4, 5, 6]
print(f"Original list: {list1}")

# METHOD 1: random.sample() - Sampling WITHOUT replacement
sample1 = random.sample(list1, 1)  # Pick 1 item from list
print(f"\n1️⃣  random.sample(list1, 1): {sample1}")
print("   📝 Note: Returns a LIST, even for single item")
print("   🚫 Cannot pick the same item twice (no replacement)")

# METHOD 2: random.choices() - Sampling WITH replacement
sample2 = random.choices(list1, k=2)  # Pick 2 items (k parameter required)
print(f"\n2️⃣  random.choices(list1, k=2): {sample2}")
print("   📝 Note: Returns a LIST, uses 'k=' parameter")
print("   ✅ CAN pick the same item multiple times (with replacement)")

# METHOD 3: random.choice() - Single selection
sample3 = random.choice(list1)  # Pick exactly 1 item
print(f"\n3️⃣  random.choice(list1): {sample3}")
print("   📝 Note: Returns a SINGLE VALUE (not a list)")
print("   ⭐ Most common for picking one random item")

# DEMONSTRATION: Show the difference in action
print(f"\n🔍 DEMONSTRATION - Sampling 3 items multiple times:")
print("random.sample() - NO duplicates allowed:")
for i in range(3):
    result = random.sample(list1, 3)
    print(f"   Attempt {i+1}: {result}")

print("\nrandom.choices() - Duplicates ARE allowed:")
for i in range(3):
    result = random.choices(list1, k=3)
    print(f"   Attempt {i+1}: {result}")

# ANSWER THE QUESTIONS
print(f"\n❓ QUESTION ANSWERS:")
print("Q: Would it ever choose the same list item twice?")
print("A: • random.sample() = NO (sampling without replacement)")
print("   • random.choices() = YES (sampling with replacement)")
print("   • random.choice() = N/A (only picks one item)")
print()
print("Q: What's the difference between choices() and sample() other than k?")
print("A: • sample() = No duplicates possible")
print("   • choices() = Duplicates allowed")
print("   • sample() uses regular parameter, choices() requires k=")

print("\n" + "=" * 80)
print("📊 PART 2: PANDAS DATA ANALYSIS")
print("=" * 80)

# Load the penguin dataset
try:
    data = pd.read_csv('penguins_size.csv')
    print("✅ Dataset loaded successfully!")
except FileNotFoundError:
    print("❌ Error: penguins_size.csv not found!")
    print("   Make sure the file is in your current directory")
    exit()

# Basic dataset information
print(f"\n📋 DATASET OVERVIEW:")
print(f"Shape: {data.shape} (rows × columns)")
print(f"Columns: {list(data.columns)}")
print(f"Data types:\n{data.dtypes}")

# Examine missing data
print(f"\n🔍 MISSING DATA ANALYSIS:")
missing_data = data.isnull().sum()
print(missing_data)
print(f"\nTotal missing values: {missing_data.sum()}")
print(f"Percentage missing: {(missing_data.sum() / (len(data) * len(data.columns))) * 100:.2f}%")

# Show which columns have missing data
columns_with_missing = missing_data[missing_data > 0]
if len(columns_with_missing) > 0:
    print(f"\nColumns with missing data:")
    for col, count in columns_with_missing.items():
        percentage = (count / len(data)) * 100
        print(f"   • {col}: {count} missing ({percentage:.1f}%)")

print(f"\nOriginal dataset: {len(data)} rows")

# Clean the data by removing rows with ANY missing values
data1 = data.dropna()
print(f"After removing rows with missing data: {len(data1)} rows")
print(f"Rows removed: {len(data) - len(data1)}")

# Verify cleaning worked
print(f"\nVerification - missing values after cleaning:")
print(data1.isnull().sum())
print(f"✅ Total missing values: {data1.isnull().sum().sum()}")

print("\n" + "=" * 80)
print("📈 PART 3: DATA VISUALIZATION")
print("=" * 80)

# Prepare data for visualization
species_counts = data.species.value_counts()  # Using original data for species counts
print(f"\nSpecies distribution in dataset:")
for species, count in species_counts.items():
    percentage = (count / len(data)) * 100
    print(f"   🐧 {species}: {count} penguins ({percentage:.1f}%)")

print(f"\n🎨 Creating visualizations...")

# 1. PIE CHART - Method 1 (Basic matplotlib)
print("1️⃣  Creating pie chart (matplotlib)...")
plt.figure(figsize=(10, 8))
plt.pie(species_counts.values, labels=species_counts.index, startangle=90)
plt.title('Penguin Species Distribution - Basic Pie Chart', fontsize=14, pad=20)
plt.axis('equal')
plt.tight_layout()
plt.show()

# 2. PIE CHART - Method 2 (Pandas with percentages)
print("2️⃣  Creating pie chart with percentages...")
plt.figure(figsize=(10, 8))
species_counts.plot(kind="pie", autopct='%.2f%%', startangle=90)
plt.title('Penguin Species Distribution - With Percentages', fontsize=14)
plt.ylabel('')  # Remove default ylabel
plt.tight_layout()
plt.show()

# 3. BAR CHART
print("3️⃣  Creating bar chart...")
plt.figure(figsize=(10, 6))
bars = plt.bar(species_counts.index, species_counts.values, color=['skyblue', 'lightcoral', 'lightgreen'])
plt.title('Penguin Species Count - Bar Chart', fontsize=14, pad=20)
plt.xlabel('Species', fontsize=12)
plt.ylabel('Number of Penguins', fontsize=12)

# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 1,
             f'{int(height)}', ha='center', va='bottom')

plt.tight_layout()
plt.show()

# 4. HISTOGRAM - Method 1 (Matplotlib)
print("4️⃣  Creating histogram (matplotlib)...")
plt.figure(figsize=(10, 6))
plt.hist(data['culmen_length_mm'].dropna(), bins=8, alpha=0.7, edgecolor='black')
plt.title('Culmen Length Distribution - Histogram (matplotlib)', fontsize=14)
plt.xlabel('Culmen Length (mm)', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

# 5. HISTOGRAM - Method 2 (Seaborn)
print("5️⃣  Creating histogram (seaborn)...")
plt.figure(figsize=(10, 6))
sns.histplot(data=data, x='culmen_length_mm', bins=8)
plt.title('Culmen Length Distribution - Histogram (seaborn)', fontsize=14)
plt.tight_layout()
plt.show()

# 6. KDE PLOT (Kernel Density Estimation)
print("6️⃣  Creating KDE plot...")
plt.figure(figsize=(10, 6))
sns.kdeplot(data=data, x='culmen_length_mm', fill=True, alpha=0.6)
plt.title('Culmen Length Distribution - KDE Plot (Smooth Density)', fontsize=14)
plt.xlabel('Culmen Length (mm)', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.tight_layout()
plt.show()

# 7. SCATTER PLOT - Basic (Matplotlib)
print("7️⃣  Creating basic scatter plot...")
plt.figure(figsize=(10, 6))
plt.scatter(data['culmen_length_mm'], data['culmen_depth_mm'], alpha=0.6)
plt.title('Culmen Length vs Depth - Basic Scatter Plot', fontsize=14)
plt.xlabel('Culmen Length (mm)', fontsize=12)
plt.ylabel('Culmen Depth (mm)', fontsize=12)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# 8. SCATTER PLOT - Advanced (Seaborn with species coloring)
print("8️⃣  Creating advanced scatter plot with species coloring...")
plt.figure(figsize=(12, 8))
sns.scatterplot(x='culmen_length_mm', y='culmen_depth_mm', 
                data=data1, hue='species', s=80, alpha=0.8)
plt.title('Culmen Length vs Depth by Species - Advanced Scatter Plot', fontsize=14)
plt.xlabel('Culmen Length (mm)', fontsize=12)
plt.ylabel('Culmen Depth (mm)', fontsize=12)
plt.legend(title='Species', title_fontsize=12, fontsize=11)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

print("\n" + "=" * 80)
print("📚 SUMMARY & KEY LEARNINGS")
print("=" * 80)

print(f"""
🎯 RANDOM SAMPLING RECAP:
   • random.sample(list, n)    → No duplicates, returns list
   • random.choices(list, k=n) → Allows duplicates, returns list  
   • random.choice(list)       → Single item, returns value

📊 DATA ANALYSIS RECAP:
   • Original dataset: {len(data)} penguins
   • After cleaning: {len(data1)} penguins ({len(data)-len(data1)} rows removed)
   • Species: {', '.join(species_counts.index)}
   • Most common: {species_counts.index[0]} ({species_counts.iloc[0]} penguins)

📈 VISUALIZATION TYPES LEARNED:
   1. Pie Charts     → Show proportions/percentages
   2. Bar Charts     → Compare categories side-by-side
   3. Histograms     → Show distribution of continuous data
   4. KDE Plots      → Smooth version of histogram (density)
   5. Scatter Plots  → Show relationships between two variables
   
🌟 ADVANCED TECHNIQUES:
   • Using 'hue' parameter to color by categories
   • Adding percentages to pie charts with autopct
   • Customizing plot appearance with titles, labels, colors
   • Handling missing data before visualization

💡 NEXT STEPS:
   • Try other seaborn plot types: boxplot, violinplot, pairplot
   • Experiment with different color palettes
   • Add statistical trend lines to scatter plots
   • Create subplots to compare multiple visualizations
""")

print("🎉 Lab completed successfully!")
print("=" * 80)