import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Salaries.csv')

# df = df.to_numpy()
##################################
# 1- Basic Data Exploration: Identify the number of rows and columns in the dataset,
# determine the data types of each column, and check for missing values in each column

print('Task 1: ')
print()
no_rows_columns = df.shape  #(rows,columns)
print('(rows,columns)')
print(no_rows_columns)
print()
print("Column:                Type:")
print(df.dtypes)
print()
print("Column:     No.missing values:")
print(df.isnull().sum())
print('##################################')
print()
##################################

# 2- Descriptive Statistics: Calculate basic statistics mean, median, mode, minimum,
# and maximum salary, determine the range of salaries, and find the standard deviation.
print('Task 2: ')

mean_salary = df['TotalPay'].mean()
print('Mean of salaries is: ', mean_salary)

median_salary = df['TotalPay'].median()
print('Median of salaries is: ',median_salary)

mode_of_salaries = df['TotalPay'].mode()[0]
print('Mode of salaries is: ',mode_of_salaries)

minimum_salary = df['TotalPay'].min()
print('Minimum salary is:', minimum_salary)

maximum_salary = df['TotalPay'].max()
print('Maximum salary is: ', maximum_salary)

range_of_salaries = maximum_salary-minimum_salary
print('Range of salaries is: ', range_of_salaries)

standard_deviation = df['TotalPay'].std()
print('Standard deviation of salaries is: ', standard_deviation)
print('##################################')
print()

##################################

# 3- Data Cleaning: Handle missing data by suitable method with explain why you use it

print('Task 3: ')

# Droping 4 rows from this data set isn't effective but in rest columns will replace NA with mode value
df = df.dropna(subset=['OvertimePay'])
df['BasePay'] = df['BasePay'].fillna(df['BasePay'].mode()[0])
df['Benefits'] = df['Benefits'].fillna(df['Benefits'].mode()[0])

# now we have 'Notes' and 'Status' and both have NA in all rows so we will put 0 in all rows

df['Notes'] = df['Notes'].fillna(0)
df['Status'] = df['Status'].fillna(0)

# now we have a clear data
print('Data after cleaning')
print("Column:     No.missing values:")
print(df.isnull().sum())

print('##################################')
print()

##################################

# 4- Basic Data Visualization: Create histograms or bar charts to visualize the distribution of salaries,
# and use pie charts to represent the proportion of employees in different departments.

plt.hist(df['TotalPay'],bins=30, color='blue', edgecolor='black')
plt.xlabel('Total Pay')
plt.ylabel('Frequency')
plt.title('Distribution of salaries')
plt.show()

# this line to convert all job titles to lowercase as there were jobs with the same name in uppercase in rows
# and in lowercase in another rows

df['JobTitle'] = df['JobTitle'].str.lower()
department_counts = df['JobTitle'].value_counts()
# this to let chart more readable and drop noise data
filtered_departments = department_counts[department_counts >= 1000]
plt.figure(figsize=(8, 8))
plt.pie(filtered_departments, labels=filtered_departments.index, autopct='%1.1f%%', startangle=140)
plt.title('Proportion of Employees in Different Departments')
plt.show()

##################################

# 5- Grouped Analysis: Group the data by one or more columns and calculate summary statistics for each group,
# and compare the average salaries across different groups.

print('Task 5: ')

grouped_df = df.groupby('JobTitle')
summary_statistics = grouped_df['TotalPay'].agg(['mean', 'median', 'std'])
print(summary_statistics)

print('##################################')
print()

##################################

# 6- Simple Correlation Analysis: Identify any correlation between salary and another numerical column,
# and plot a scatter plot to visualize the relationship

print('Task 6: ')

corr_salary_and_basepay = df['TotalPay'].corr(df['BasePay'])
print('correlation between salary and base pay is: ', corr_salary_and_basepay)

plt.scatter(df['TotalPay'], df['BasePay'])
plt.xlabel('TotalPay')
plt.ylabel('BasePay')
plt.title('Scatter Plot of Total Pay vs Base Pay')
plt.show()

print('##################################')
print()
#################################


# 7- Summary of Insights: Write a brief report summarizing the findings and insights from the analyses.

print('Task 7: ')

print('Summary :')
print('- Data has a low number of NAs so it shows that this data is more accurate.')
print('- Salary with 0 is more than 25k which means this company offers free training.')
print('- This company may be stable and established in 2011 as it is the oldest year.')
print('- When the base salary is high the total salary will be also high in most cases.')
print('- Job with the most employees is the transit operator')

print('##################################')

#################################
