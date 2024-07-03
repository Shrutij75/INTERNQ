#import the required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#load the dataset in the form of data frame
df=pd.read_csv("C:\\Users\\DELL\\Downloads\\iris_dataset.csv")
print(df)

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

#pairplot
print("\nPairplot of the Iris dataset:")
sns.pairplot(df, markers=["o", "s", "D"])
plt.suptitle('Pairplot of Iris Dataset', y=1.02)
plt.show()

#heatmap defines the correlation between the columns or attributes
print("--HEATMAP IS---")
print("\nCorrelation matrix of the Iris dataset:")
correlation_matrix = df.drop('target',axis=1).corr()
sns.heatmap(correlation_matrix, annot=True,cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix of Iris Dataset')
plt.show()
