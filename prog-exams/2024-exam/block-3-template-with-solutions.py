##############################
# 30M015 Exam 2024, Block 3. #
##############################

# Grading (do not remove):
# a) 1
# b) 1
# c) 1
# d) 1
# e) 1
# f) 1

snr = 1234567  # replace with your student number

import pandas as pd
df = pd.read_csv("sales-data-2024.csv")

### Question a) ###
# Compute and print the average number of units sold per day:
print(df['sales'].mean())


### Question b) ###
# Create a new variable in df called daily_revenue:
df['daily_revenue'] = df['price'] * df['sales']

### Question c) ###
# Compute and print the mean daily revenue in the dataset:
print(df['daily_revenue'].mean())

### Question d) ###
# Compute and print the total number of units sold in May 2024:
print(df[(df['year'] == 2024) & (df['month'] == 5)]['sales'].sum())

# or split it up into steps:
may = df['month'] == 5
year_2024 = df['year'] == 2024
may_2024 = [i and j for i, j in zip(may, year_2024)]
df_may_2024 = df.loc[may_2024]
print(df_may_2024['sales'].sum())

### Question e) ###
# Create a new variable in df called weekend:

# All of the following work:
df['weekend'] = [i in ['Sat', 'Sun'] for i in df['day_of_week']]
df['weekend'] = [i == 'Sat' or i == 'Sun' for i in df['day_of_week']]
df['weekend'] = (df['day_of_week'] == 'Sat') | (df['day_of_week'] == 'Sun')
df['weekend'] = df['day_of_week'].isin(['Sat', 'Sun'])

### Question f) ###
# Compute and print the average daily sales on days that are NOT the weekend:
print(df[~df['weekend']]['sales'].mean())

# or split it up into steps:
not_weekend = [not i for i in df['weekend']]
df_not_weekend = df.loc[not_weekend]
print(df_not_weekend['sales'].mean())

