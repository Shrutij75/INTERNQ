#import the required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#load the dataset in the form of data frame
df=pd.read_csv("C:\\Users\\DELL\\Downloads\\Employee.csv")
#print(df)

#head() used to show the first few rows of the dataset
print(df.head())

#info()is used to find the basic information about the columns of the dataset
print(df.info())

#describe() is used for printing the summary statitics
print("---SUMMARY STATITICS----")
print(df.describe())

#check if any missing or null value is present or not.
print(df.isnull().sum())

# hist() is used for plotting histogram
print("--HISTOGRAM IS---")
df.hist(figsize=(10,8))
plt.show()

#for plotting boxplot
print("--BOXPLOT IS---")
plt.figure(figsize=(10,6))
plt.title("BOXPLOT")
sns.boxplot(data=df)
plt.show()

#heatmap defines the correlation between the columns or attributes
print("--HEATMAP IS---")
print("\nCorrelation matrix of the dataset:")
correlation_matrix = df.drop(['Name','Department'],axis=1).corr()
sns.heatmap(correlation_matrix, annot=True,cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix of Dataset')
plt.show()

#group by department and calculate the mean
'''as in calculating mean we have to focused thatt all the columns have numeric data so 
the column 'Name' have string type object.'''
numeric_df = df.drop(['Name'], axis=1) 
print(numeric_df.groupby('Department').mean())

# #salry distribution by department
plt.figure(figsize=(10,6))
sns.boxplot(x='Department',y='Salary',data=df)
plt.title("salary by department")
plt.show()

#year_of_experience distribution by department
plt.figure(figsize=(10,6))
sns.boxplot(x='Department',y='Years_Experience',data=df)
plt.title("year_of_experience  by department")
plt.show()

#Salary vs Years_of_Experience
plt.figure(figsize=(10,6))
sns.scatterplot(x='Years_Experience',y='Salary',hue='Department',data=df)
plt.title("Salary VS Years_Experience")
plt.show()