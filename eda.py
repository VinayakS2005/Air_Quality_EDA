import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('REAL_TIME_AIR_QUALITY_INDEX.csv', encoding='latin-1', on_bad_lines='skip')

df.rename(columns={'pm10_concentration': 'pm10', 'pm25_concentration': 'pm25', 'no2_concentration': 'no2'}, inplace=True)

# Filter out data from year 2000 onwards for PM2.5 analysis
pm25_df = df[['year', 'pm25']].dropna()
pm25_df = pm25_df[pm25_df['year'] >= 2000]
pm25_avg = pm25_df.groupby('year', as_index=False)['pm25'].mean()

# Plotting PM2.5 trend from 2000 onwards
plt.figure(figsize=(12, 6))
sns.lineplot(data=pm25_avg, x='year', y='pm25', marker='o')
plt.title('Average PM2.5 Trend (2000 Onwards)')
plt.xlabel('Year')
plt.ylabel('Average PM2.5 Level')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
# PM10 analysis
pm10_df = df[['year', 'pm10']].dropna()
pm10_df = pm10_df[pm10_df['year'] >= 2000]
pm10_avg = pm10_df.groupby('year', as_index=False)['pm10'].mean()

# Plotting PM10 trend from 2000 onwards
plt.figure(figsize=(10, 5))
sns.lineplot(data=pm10_avg, x='year', y='pm10', label='PM10', color='orange')
plt.title('Average PM10 Trend Over Time (2000 Onwards)')
plt.xlabel('Year')
plt.ylabel('Average PM10 Level')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plotting Histogram with KDE for each pollutant
plt.figure(figsize=(12, 6))
sns.histplot(
    data=melted_df,
    x='Level',
    hue='Pollutant',
    kde=True,
    element='step',
    stat='density',
    common_norm=False
)
plt.title('Distribution of Pollutant Levels (0–100)')
plt.xlabel('Pollutant Level')
plt.ylabel('Density')
plt.xlim(0, 100)
plt.tight_layout()
plt.show()

# Subplots for individual pollutant distributions (Histograms with KDE)
plt.figure(figsize=(16, 12))
for i, pollutant in enumerate(available_pollutants, 1):
    plt.subplot(3, 2, i)  # Adjust if more pollutants
    sns.histplot(
        data=df[df[pollutant] <= 100],  # Filter values between 0 and 100
        x=pollutant,
        kde=True,
        bins=30,
        color=sns.color_palette("husl")[i - 1],
        stat="frequency",
        element="step",
        fill=True,
        alpha=0.5,
        linewidth=1.5
    )
    plt.title(f'{pollutant.upper()} Distribution', fontsize=14)
    plt.xlabel('Level')
    plt.ylabel('Frequency')
    plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.suptitle("Individual Pollutant Level Distributions (0–100)", fontsize=18, y=1.02)
plt.show()

# Box plot for pollutant distribution comparison
plt.figure(figsize=(12, 6))
sns.boxplot(
    x='Pollutant',
    y='Level',
    data=melted_df,
    palette='Set2',
    linewidth=2,
    fliersize=3,
    boxprops=dict(alpha=0.7)
)
plt.title('Pollutant Distribution - Boxplot', fontsize=16, fontweight='bold')
plt.xlabel('Pollutant', fontsize=12)
plt.ylabel('Pollutant Level')
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.show()
pollutant_tempcov_columns = ['pm10_tempcov', 'pm25_tempcov', 'no2_tempcov']

df_tempcov = df[pollutant_tempcov_columns].dropna()

correlation_matrix = df_tempcov.corr()

# Plotting the correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5, fmt=".2f", cbar_kws={'shrink': 0.8})
plt.title('Correlation Matrix for pm10_tempcov, pm25_tempcov, and no2_tempcov')
plt.tight_layout()
plt.show()
