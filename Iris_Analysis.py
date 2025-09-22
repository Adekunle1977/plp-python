# ---------------------------------------------------
# Assignment: Data Analysis with Pandas & Matplotlib
# Dataset: Iris Dataset
# ---------------------------------------------------

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# ---------------------------------------------------
# Task 1: Load & Explore Data
# ---------------------------------------------------

print("=== TASK 1: LOAD & EXPLORE DATA ===\n")

# Load Iris dataset from sklearn
iris = load_iris(as_frame=True)
df = iris.frame  # Convert to pandas DataFrame

# Save dataset to CSV (to satisfy requirement of using CSV)
df.to_csv("iris.csv", index=False)

# Try-except for error handling
try:
    df = pd.read_csv("iris.csv")
    print("Dataset loaded successfully!\n")
except FileNotFoundError:
    print("Error: Dataset file not found.")

# Display first few rows
print("First 5 rows of dataset:")
print(df.head())

# Dataset structure
print("\nDataset Info:")
print(df.info())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Clean missing values (drop rows with NaN if any)
df = df.dropna()
print("\nAfter cleaning, missing values:")
print(df.isnull().sum())

# ---------------------------------------------------
# Task 2: Basic Data Analysis
# ---------------------------------------------------

print("\n=== TASK 2: BASIC DATA ANALYSIS ===\n")

# Basic statistics
print("\nBasic Statistics:")
print(df.describe())

# Grouping by species (target column) and computing mean
group_means = df.groupby("target").mean()
print("\nMean values grouped by species (target):")
print(group_means)

# Map numeric labels to species names
species_map = dict(zip(range(3), iris.target_names))
df["species"] = df["target"].map(species_map)

# Findings
print("\nPatterns / Findings:")
print("- Setosa species tend to have smaller petal length and width.")
print("- Virginica species have the largest petals on average.")
print("- Sepal length varies more gradually across species compared to petal length.")

# ---------------------------------------------------
# Task 3: Data Visualization
# ---------------------------------------------------

print("\n=== TASK 3: DATA VISUALIZATION ===\n")

sns.set(style="whitegrid")

# 1. Line Chart: Petal length trend across samples
plt.figure(figsize=(8,5))
plt.plot(df.index, df["petal length (cm)"], label="Petal Length", color="red")
plt.title("Petal Length Trend Across Samples")
plt.xlabel("Sample Index")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.show()

# 2. Bar Chart: Average petal length per species
plt.figure(figsize=(8,5))
df.groupby("species")["petal length (cm)"].mean().plot(kind="bar", color=["red","green","blue"])
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram: Distribution of sepal length
plt.figure(figsize=(8,5))
plt.hist(df["sepal length (cm)"], bins=15, color="purple", edgecolor="black")
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot: Sepal length vs Petal length
plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x="sepal length (cm)", y="petal length (cm)", hue="species", palette="Set2")
plt.title("Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()

# ---------------------------------------------------
# Observations
# ---------------------------------------------------

print("\n=== OBSERVATIONS ===")
print("- The dataset contains 150 rows and 5 columns (4 features + target).")
print("- No missing values were found.")
print("- Petal length is the most distinguishing feature between species.")
print("- Setosa has very distinctively small petals compared to Versicolor and Virginica.")
