# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Read data from CSV`
df = pd.read_csv('https://raw.githubusercontent.com/yeswanth2727/Laptop-Specifications-Data-Analysis-Report/refs/heads/main/Data%20Set/laptop_prices.csv')
df.head()

# Check for duplicate rows
duplicate_rows = df.duplicated()

# Remove duplicate rows
df.drop_duplicates(inplace=True)

9# Display information about the DataFrame
df.info()

# Display basic statistics of the DataFrame
df.describe()


def plot_heatmap(df):
    # Select only numeric columns for the correlation matrix
    numeric_df = df.select_dtypes(include='number')
    correlation_matrix = numeric_df.corr()

    # Set up the matplotlib figure
    plt.figure(figsize=(10, 8))

    # Create a heatmap
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)

    # Add title and labels for clarity
    plt.title("Heatmap of Feature Correlations")
    plt.show()

# Example usage:
# Assuming df is your DataFrame
plot_heatmap(df)

def plot_type_name_pie_chart(df):
    # Count values for the TypeName column
    type_name_counts = df['TypeName'].value_counts()
    
    # Plot the pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(type_name_counts, labels=type_name_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title("Proportion of each TypeName Category")
    plt.show()

# Example usage:
plot_type_name_pie_chart(df)

# Line Plot Function
def plot_line(df, x_column, y_column):
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x=x_column, y=y_column)
    plt.title(f"{y_column} vs {x_column}")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.show()

# Line plot for Price over Inches
plot_line(df, 'Inches', 'Price_euros')   
