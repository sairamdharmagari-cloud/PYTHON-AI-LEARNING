#we're going to combine NumPy + Pandas + Matplotlib into one project
#  This is a great checkpoint before moving deeper into AI/ML.

'''Load data'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

print("----- SALES DATA -----")
print(df)

'''Basic analysis'''

print("\n----- BASIC ANALYSIS -----")

print("Total sales:", df["Sales"].sum())
print("Average sales:", df["Sales"].mean())
print("Highest sale:", df["Sales"].max())
print("Lowest sale:", df["Sales"].min())

'''Find the beat selling product'''

best_index = df["Sales"].idxmax()

print("\n----- BEST PRODUCT -----")
print("Product:", df.loc[best_index, "Product"])
print("Sales:", df.loc[best_index, "Sales"])

'''Category analysis'''
#use groupby()

category_sales = df.groupby("Category")["Sales"].sum()

print("\n----- CATEGORY SALES -----")
print(category_sales)


'''Calculate Revenue per Unit'''
'''We have total sales and quantity.'''

#Create:
df["Sales_Per_Unit"] = df["Sales"] / df["Quantity"]

print("\n----- SALES PER UNIT -----")
print(df[["Product", "Sales_Per_Unit"]])

#NumPy

#Let's use NumPy to calculate the standard deviation:

sales_array = np.array(df["Sales"])

print("\nSales Standard Deviation:")
print(np.std(sales_array))

#So you're now using:

#Pandas → Data handling
#NumPy  → Numerical calculations

#Create a Bar Chart 
plt.bar(df["Product"], df["Sales"])

plt.xlabel("Product")
plt.ylabel("Sales")
plt.title("Product Sales")

plt.xticks(rotation=45)

plt.show()

#rotation=45 makes the product names easier to read.

'''Your Data Science workflow so far

You've now learned this pipeline:

                  DATA
                    ↓
              CSV Dataset
                    ↓
                Pandas
          ┌─────────┴─────────┐
          ↓                   ↓
      Cleaning            Analysis
          ↓                   ↓
        NumPy              GroupBy
          └─────────┬─────────┘
                    ↓
               Matplotlib
                    ↓
             📊 Visualization'''