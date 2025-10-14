Pandas Interview Questions for Freshers

1. What is Pandas in Python?
Pandas is a powerful open-source data analysis and manipulation library for Python. It provides data structures like Series and DataFrame for handling structured data, making tasks like data cleaning, transformation, and visualization straightforward and efficient. Pandas is widely used in data science, finance, and many other fields for their robust data-handling capabilities.

2. What is Series in Pandas?
A Series in Pandas is a one-dimensional array-like object that can hold data of any type (integers, strings, floats, etc.). Each element in a Series is associated with a unique label, called an index, which can be used to access individual elements.

For example,

import pandas as pd<br>
a = [1, 7, 2]<br>
myvar = pd.Series(a)<br>
print(myvar)
​

Output of Series in Pandas

3. What is a DataFrame in Pandas?
A DataFrame in Pandas is a 2-dimensional, size-mutable, and heterogeneous tabular data structure with labeled axes (rows and columns). It is similar to a table in a database or a data frame in R. Each column can contain different data types.

2-dimensional DataFrame means it has rows and columns like a table; size-mutable means that we can add or remove rows and columns; and heterogeneous means that different columns can hold different types of data (e.g., integers, strings, floats).

import pandas as pd<br>
data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}<br>
df = pd.DataFrame(data)<br>
print(df)
Output of DataFrames in Pandas

4. How do you iterate over DataFrame in Pandas?
To iterate over a DataFrame in Pandas, you can use several methods. Each method serves different purposes and has its advantages in terms of readability and performance.

iterrows(): Iterates over DataFrame rows as (index, Series) pairs.
itertuples(): Iterates over DataFrame rows as namedtuples.
apply(): Applies a function along an axis of the DataFrame.
items(): Iterates over DataFrame columns as (column name, Series) pairs.
Get 100% Hike!

Master Most in Demand Skills Now!

Email Address

Phone Number
By providing your contact details, you agree to our Terms of Use & Privacy Policy
5. How do you select a single column named 'Age' from a DataFrame called df?
To select a single column named ‘Age’ from a DataFrame called ‘df’, you can use square brackets and the column name like this:

age_column = df['Age']
This will create a new variable ‘age_column’ containing the values from the ‘Age’ column of the DataFrame ‘df’.

6. What is the difference between Series and DataFrame?
Series DataFrame
1-dimensional labeled array 2-dimensional labeled data structure
Contains data of a single data type Can contain data of multiple data types across columns
Single column of data Multiple columns, each can be of different data types
Indexed by a single axis (labels) Indexed by two axes (rows and columns)
Created using pd.Series() Created using pd.DataFrame()
7. What is an index in Pandas?
In Pandas, an index is a fundamental data structure that labels and identifies rows or elements within a DataFrame or Series. It provides a way to uniquely identify each row, enabling efficient data retrieval, alignment, and manipulation. Indexing facilitates easy access, selection, and alignment of data in Pandas data structures.

8. Explain MultiIndexing in Pandas.
MultiIndexing in Pandas allows creating a DataFrame with multiple levels of indexes, providing a way to represent higher-dimensional data in a tabular structure. It’s particularly useful for handling complex datasets with hierarchical row or column labels. MultiIndexing facilitates advanced data manipulation, selection, and aggregation operations across different levels of the index hierarchy efficiently.

9. What is reindexing in Pandas?
Reindexing in Pandas is the process of altering the index of a DataFrame or Series to match a new set of labels. It can be used to rearrange data according to a new index or to align data from multiple sources. Reindexing allows for handling missing data, aligning different datasets, and reshaping data structures to facilitate analysis.

Syntax: df.reindex(new_index)

10. Why is there no parenthesis in DataFrame.shape?
The absence of parentheses in “DataFrame.shape” is because it’s an attribute, not a method. In Python, attributes are accessed without parentheses, while methods require them. “DataFrame.shape” returns a tuple representing the dimensions of the DataFrame, typically in the form of rows or columns.

11. What are the different ways to create a Series?
Using a list or array: Create a Series from a Python list or NumPy array.
Using a dictionary: Convert a dictionary into a Series where keys become index labels.
Using scalar value: Repeat a scalar value to create a series of specified lengths.
Using a DataFrame column: Extract a column from a DataFrame to create a Series.
Using a file or URL: Read data from a file or URL into a Series.
1. Using a list or array:

import pandas as pd<br>
my_list = [10, 20, 30, 40, 50]<br>
series_from_list = pd.Series(my_list)
2. Using a dictionary:

import pandas as pd<br>
my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 50}<br>
series_from_dict = pd.Series(my_dict)
3. Using scalar value:

import pandas as pd<br>
series_from_scalar = pd.Series(5, index=[0, 1, 2, 3, 4])
4. Using a DataFrame column:

import pandas as pd<br>
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],<br>
'Age': [25, 30, 35, 40]}<br>
df = pd.DataFrame(data)<br>
series_from_df = df['Age']
5. Using a file or URL:

import pandas as pd<br>
url = '<https://example.com/data.csv>'<br>
series_from_file = pd.read_csv(url, squeeze=True)
12. What are the different ways to create a DataFrame in Pandas?
From a Dictionary: Create a DataFrame by passing a dictionary of lists as input.
From a List of Lists: Construct a DataFrame from a list of lists.
From a List of Dictionaries: Convert a list of dictionaries into a DataFrame.
From a NumPy Array: Generate a DataFrame from a NumPy array.
From a CSV File: Read data from a CSV file into a DataFrame using “pd.read_csv()”.
From an Excel File: Load data from an Excel file using “pd.read_excel()”.

1. From a Dictionary:

import pandas as pd<br>
data = {'Name': ['Alice', 'Bob', 'Charlie'],<br>
'Age': [25, 30, 35],<br>
'City': ['New York', 'Los Angeles', 'Chicago']}<br>
df = pd.DataFrame(data)
2. From a List of Lists:

import pandas as pd<br>
data = [['Alice', 25, 'New York'],<br>
['Bob', 30, 'Los Angeles'],<br>
['Charlie', 35, 'Chicago']]<br>
df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
3. From a List of Dictionaries:

import pandas as pd<br>
data = [{'Name': 'Alice', 'Age': 25, 'City': 'New York'},<br>
{'Name': 'Bob', 'Age': 30, 'City': 'Los Angeles'},<br>
{'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}]<br>
df = pd.DataFrame(data)
4. From a NumPy Array:

import pandas as pd<br>
import numpy as np<br>
data = np.array([['Alice', 25, 'New York'],<br>
['Bob', 30, 'Los Angeles'],<br>
['Charlie', 35, 'Chicago']])<br>
df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
5. From a CSV File:

import pandas as pd<br>
df = pd.read_csv('data.csv')
6. From an Excel File:

import pandas as pd<br>
df = pd.read_excel('data.xlsx')
13. How do you read data into a DataFrame from a CSV file?
A CSV file, or “Comma Separated Values,” can be used to generate a data frame. This can be accomplished by passing the CSV file as an argument to the read_csv() method.
pandas.read_csv(file_name)

Alternatively, you can use the read_table() method, which accepts a CSV file as an input along with a delimiter value.
pandas.read_table(file_name, delimiter)

Pandas Interview Questions for Experienced
14. What are some limitations of Pandas?
Memory Usage: Pandas can be memory-intensive, struggling with large datasets that exceed available RAM.
Speed: Processing speed can be slower compared to low-level languages like C or C++.
Performance: Certain operations, such as group-by and pivot tables, may lack efficiency on large datasets.
Limited Visualization: Direct visualization capabilities are not as advanced as specialized libraries like Matplotlib or Seaborn.
Data Cleaning Challenges: Handling missing or inconsistent data can be cumbersome and time-consuming.
15. Explain categorical data in Pandas.
In Pandas, categorical data represents variables with a fixed and finite set of unique values, like gender or color. It optimizes memory usage and can speed up operations like “groupby” and “value_counts”. Pandas assign a numerical code to each category, making computations more efficient while retaining the original labels for readability and analysis.

16. Give a brief description of the time series in Pandas.
In Pandas, a time series is a one-dimensional array-like data structure where each element is associated with a timestamp or a specific time period. It’s commonly used for analyzing and manipulating time-based data, such as stock prices, temperature readings, or website traffic over time. Pandas offers powerful tools for indexing, slicing, and analyzing time series data efficiently.

17. How can we convert Series to DataFrame?
To convert a Pandas Series to a DataFrame, use the “to_frame()” method. This method converts the Series into a DataFrame with a single column.

For example, if “s” is a Series, “df = s.to_frame()” will create a DataFrame “df” with the Series “s” as its column. Optionally, specify a column name: “df = s.to_frame(‘column_name’)”.

Let’s see the code for the same:

import pandas as pd<br>

# Create a pandas Series<br>

s = pd.Series([1, 2, 3, 4, 5])<br>

# Convert the Series to a DataFrame<br>

df = s.to_frame()<br>

# Display the DataFrame<br>

print(df)
Output:

0
0 1
1 2
2 3
3 4
4 5

18. What is TimeDelta?
TimeDelta is a data type used to represent the difference between two points in time. It measures the duration, typically in days, seconds, and microseconds. It’s commonly employed in programming languages like Python to perform arithmetic operations on dates and times, facilitating tasks such as calculating intervals or scheduling events.

19. How can we convert DataFrame to an Excel file?
To convert a DataFrame to an Excel file in Python, you can use the “to_excel()” function from the Pandas library. First, import Pandas, then use “DataFrame.to_excel()” with the file path specified to save the DataFrame to an Excel file.

For example,

import pandas as pd<br>

# Create a DataFrame<br>

data = {'Name': ['John', 'Emma', 'Peter'],<br>
'Age': [30, 25, 35],<br>
'City': ['New York', 'London', 'Paris']}<br>
df = pd.DataFrame(data)<br>

# Convert DataFrame to Excel<br>

df.to_excel('example.xlsx', index=False)
This code snippet creates a DataFrame with columns for Name, Age, and City. Then, it saves this DataFrame to an Excel file named “example.xlsx” without including the index.

20. How can you retrieve the top six rows and bottom seven rows in Pandas DataFrame?
To retrieve the top six rows of a Pandas DataFrame, use the .head(6) method.
For the bottom seven rows, utilize the .tail(7) method.
21. How do you read text files with Pandas?
To read text files with Pandas, you can use the “read_csv()” function, which is versatile enough to handle various text-based file formats. For example, to read a comma-separated values (CSV) file named “data.csv,” you can simply use:

import pandas as pd<br>

# Read the CSV file into a DataFrame<br>

df = pd.read_csv('data.csv')
Pandas automatically infers the delimiter from the file extension.

However, if your file has a different delimiter, you can specify it using the “sep” parameter, like “pd.read_csv(‘data.txt’, sep=’\t’)” for tab-separated files.

Additionally, you can customize other parameters, like headers, indexes, column names, etc., according to your file’s structure. This flexibility makes Pandas an excellent choice for reading and manipulating text-based data files efficiently.

22. What is the difference between merge() and concat() in Pandas?
Features Merge() Concat()
Purpose Combines DataFrames based on common columns or indices Combines DataFrames along a particular axis
Similar to SQL JOIN operation (INNER, OUTER, LEFT, RIGHT) UNION operation
Key Column Requires specifying keys to merge on Does not require keys, concatenates along axis
Axis Operates primarily along columns (axis=1) Operates along both rows (axis=0) and columns (axis=1)
Syntax Example pd.merge(df1, df2, on=’key’) pd.concat([df1, df2], axis=0)
Complexity More complex, allowing for detailed joins Simpler, primarily stacking DataFrames
Handling Indexes Aligns DataFrames based on keys Can choose to ignore or preserve indexes
Result Single DataFrame with combined data Single DataFrame with stacked data
23. How do you convert categorical values in a column into numerical ones?
To convert categorical values into numerical ones in a column, you can use techniques like label encoding or one-hot encoding.

Label Encoding: Assigns a unique number to each category.

For example,

Category A: 0
Category B: 1
Category C: 2

One-Hot Encoding: Creates new binary columns for each category, where 1 indicates the presence of the category and 0 indicates absence.

For example,

Category A: [1, 0, 0]
Category B: [0, 1, 0]
Category C: [0, 0, 1]

Label encoding is suitable when there is an ordinal relationship between categories, meaning one category is greater or better than another. One-hot encoding is appropriate when categories are unordered or when you don’t want to impose any ordinal relationship.

24. Why should standardization be performed on data, and how can you perform it using Pandas?
Standardization is important because it helps bring all features to the same scale. This is crucial for many machine learning algorithms because features with larger scales might dominate those with smaller scales, leading to biased results.

Standardization ensures that each feature has a mean of 0 and a standard deviation of 1, putting them all on a comparable scale.

To perform standardization using Pandas, you can use the “StandardScaler” class from the sci-kit-learn library, which can easily handle Pandas DataFrame objects. Here’s how you can do it:

from sklearn.preprocessing import StandardScaler<br>
import pandas as pd

# Create a DataFrame with your data<br>

data = pd.DataFrame({<br>
'feature1': [10, 20, 30, 40],<br>
'feature2': [0.1, 0.2, 0.3, 0.4]<br>
})

# Initialize StandardScaler<br>

scaler = StandardScaler()

# Fit the scaler to your data and transform it<br>

scaled_data = scaler.fit_transform(data)

# Convert the scaled data back to a DataFrame<br>

scaled_df = pd.DataFrame(scaled_data, columns=data.columns)

# Print the scaled DataFrame<br>

print(scaled_df)
This will standardize the “data” in data DataFrame and store the scaled values in “scaled_df”. Now, both “feature1” and “feature2” will have a mean of 0 and a standard deviation of 1.

25. Suppose you have a DataFrame “sales_data” with columns “Product” and “Revenue”. How can you select the first 5 rows and only the “Revenue” column?
To select the first 5 rows and only the “Revenue” column from a DataFrame “sales_data”, you can use either the “.iloc” or “.loc” method:

Using “.iloc” (integer-based indexing):

revenue_first_5 = sales_data.iloc[:5, sales_data.columns.get_loc('Revenue')]
Using “.loc” (label-based indexing):

revenue_first_5 = sales_data.loc[:4, 'Revenue']
Both of these methods will select the first 5 rows and the ‘Revenue’ column from the DataFrame `sales_data`.

26. Name some statistical functions in Pandas.
Pandas offers several statistical functions for data analysis. Some key ones include:

mean(): Calculates the average of values.
Syntax: df[‘column_name’].mean()
median(): Finds the median value.
Syntax: df[‘column_name’].median()
std(): Computes the standard deviation
Syntax: df[‘column_name’].std()
var(): Calculates the variance.
Syntax: df[‘column_name’].var()
describe(): Provides a summary of statistics for DataFrame columns.
Syntax: df.describe()
Python Pandas Interview Questions
27. Differentiate between map(), applymap(), and apply().
map() applymap() apply()
Defined only in series Defined only in DataFrame Defined in both Series and DataFrame
Accept dictionary, series, or callables only Accept callables only Accept callables only
Series.map() operates on one element at a time DataFrame.applymap() operates on one element at a time operates on entire rows or columns at a time for DataFrame, and one at a time for Series.apply
Missing values will be recorded as NaN in the output. Performs better operation than apply().  Suited to more complex operations and aggregation.
Here’s a graphical illustration of these functions:

map function

applymap function

apply function

28. How do you split a DataFrame according to a Boolean criterion?
To split a DataFrame according to a Boolean criterion in Pandas, you use conditional filtering to create two separate DataFrames based on the criterion.

Here’s a step-by-step example:

Step 1: Create a DataFrame:

import pandas as pd<br>
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],<br>
'Age': [24, 17, 35, 19]}<br>
df = pd.DataFrame(data)
Step2: Define the Boolean Criterion:

criterion = df['Age'] >= 18
Step 3: Split the DataFrame:

df_adults = df[criterion]<br>
df_minors = df[~criterion]
In this example, “df_adults” will contain rows where the “Age” is 18 or above, while “df_minors” will contain rows where the “Age” is below 18. This method allows for efficient and readable DataFrame splitting based on any Boolean condition.

29. How do you optimize performance while working with large datasets in Pandas?
To optimize performance when working with large datasets in Pandas, several strategies can be employed:

Efficient Data Types: Converting columns to more memory-efficient data types reduces memory consumption, which can significantly improve performance.
Chunk Processing: Processing data in smaller chunks rather than loading the entire dataset into memory at once helps in managing memory usage and avoids overwhelming system resources.
Vectorized Operations: Utilizing Pandas’ built-in vectorized operations instead of looping through rows leverages highly optimized C-based operations, leading to faster execution times.
Parallel Processing: Libraries like Dask or Swifter can parallelize operations, distributing the workload across multiple CPU cores and speeding up data processing tasks.
Learn how to change column data types in Pandas through this blog.

30. What is Data Aggregation in Pandas?
Data aggregation in Pandas refers to the process of summarizing, combining, or grouping data to extract meaningful insights. This typically involves operations like sum, mean, count, min, max, etc., on groups of data.

For example, consider a DataFrame `df` with columns ‘category’ and ‘values’:

import pandas as pd<br>
data = {<br>
'category': ['A', 'A', 'B', 'B', 'C', 'C'],<br>
'values': [10, 20, 30, 40, 50, 60]<br>
}
df = pd.DataFrame(data)
To aggregate the data by ‘category’ and compute the sum of ‘values’ for each category:

aggregated_data = df.groupby(‘category’).sum()

This results in:

Category    Values  

A                  30

B                  70

C                 110

Here, the data is grouped by ‘category’ and the sum of ‘values’ is calculated for each group. Aggregation helps in simplifying and summarizing large datasets for analysis.

31. What is the difference between iloc() and loc()?
Feature iloc() loc()
Purpose Index-based selection Label-based selection
Types of Indexing Integer positions Labels or Boolean arrays
Usage df.iloc[row_index, column_index] df.loc[row_label, column_label]
Primary Use Case Selecting rows and columns by numerical index Selecting rows and columns by labels
Index Type Always integers Can be strings, integers, or other data types
Example for Rows df.iloc[1:3] selects 2nd to 3rd rows df.loc[‘a’:’c’] selects rows with labels ‘a’ to ‘c’
Example for Columns df.iloc[:, 1:3] selects 2nd to 3rd columns df.loc[:, ‘col1′:’col3’] selects ‘col1’ to ‘col3’
Error Handling Raises “IndexError” if index is out of bounds Raises “KeyError” if label is not found
32. How will you sort a DataFrame?
To sort a DataFrame in Pandas, you can use the “sort_values” method. This method allows you to sort by one or more columns. You can specify the column name to sort by and the order (ascending or descending). Additionally, you can sort by index using the “sort_index” method. Here’s a basic example:

import pandas as pd<br>

# Create a sample DataFrame<br>

data = {<br>
'Name': ['John', 'Anna', 'Peter', 'Linda'],<br>
'Age': [28, 24, 35, 32]<br>
}<br>
df = pd.DataFrame(data)

# Sort by Age in ascending order<br>

sorted_df = df.sort_values(by='Age')

# Sort by Age in descending order<br>

sorted_df_desc = df.sort_values(by='Age', ascending=False)

# Sort by multiple columns (first by Age, then by Name)<br>

sorted_df_multi = df.sort_values(by=['Age', 'Name'])
print("Ascending sort by Age:\n", sorted_df)<br>
print("Descending sort by Age:\n", sorted_df_desc)<br>
print("Sort by Age, then Name:\n", sorted_df_multi)
Output:

Output of sorting of DataFrame

33. What’s the difference between interpolate() and fillna() in Pandas?
interpolate() fillna()
Fill NaN values using interpolation techniques Fill NaN values with specified values or methods
Methods: Linear, polynomial, spline, and more Methods: Constant values, forward fill, backward fill, and more
Commonly used for time series or numerical data Commonly used for replacing missing data with specific values or strategies
df.interpolate(method=’linear’) df.fillna(value=0)
34. How can we use pivot and melt data in Pandas?
In Pandas, “pivot” and “melt” functions are essential tools for reshaping data.

a. Pivot: It restructures data, typically from long to wide format, based on column values. For example, consider a DataFrame where each row represents a different date and each column represents a different city’s temperature. Using “pivot”, you can reshape this DataFrame so that each row represents a city and each column represents a date, making it easier to analyze trends over time.

pivoted_data = df.pivot(index=’Date’, columns=’City’, values=’Temperature’)

b. Melt: It performs the reverse operation of “pivot,” transforming wide data into a long format. For example, if you have a DataFrame with multiple columns representing different types of observations, “melt” can reshape it so that each row represents a single observation.

melted_data = pd.melt(df, id_vars=[‘ID’], value_vars=[‘Type1’, ‘Type2′], var_name=’Observation Type’, value_name=’Value’)

35. How do I calculate different quantile ranges in Pandas and the mean, median, mode, variance, and standard deviation?
To calculate different quantile ranges in Pandas and the mean, median, mode, variance, and standard deviation, you can use the following methods:

Quantile Ranges:  quantiles = df.quantile([0.25, 0.5, 0.75])
Mean: mean_value = df.mean()
Median:  median_value = df.median()
Mode:  mode_value = df.mode().iloc[0]
Variance: variance_value = df.var()
Standard Deviation: std_deviation_value = df.std()
Replace “df” with your DataFrame and adjust parameters as needed. These operations provide key statistical insights into your dataset.

36. How do you make label encoding using Pandas?
Label encoding is a technique used to convert categorical data into numerical format, often required by machine learning algorithms. In Pandas, label encoding can be achieved by mapping each unique category to a numerical value. This transformation simplifies data processing and analysis. Pandas provides two common methods for label encoding:

Using astype() method: This method involves converting the categorical column to a string type and then mapping each category to a numerical value using a dictionary.
Using cat.codes attribute: For categorical data stored as Pandas categorical type, label encoding can be applied directly using the cat.codes attribute, which assigns a unique numerical code to each category.
Label encoding is useful when dealing with ordinal categorical data, where the categories have a meaningful order. However, it may not be suitable for nominal categorical data with no inherent order, as it could introduce unintended relationships between the encoded values.

37. How do I create a boxplot with Pandas?
You can create a boxplot using Pandas’ `boxplot()` function, which is a wrapper around Matplotlib’s boxplot functionality. Here’s how to do it:

import pandas as pd<br>
import matplotlib.pyplot as plt

# Create a DataFrame with sample data<br>

data = {'A': [1, 2, 3, 4, 5],<br>
'B': [2, 4, 6, 8, 10]}<br>
df = pd.DataFrame(data)

# Plot a boxplot for the DataFrame<br>

df.boxplot()

# Add title and labels<br>

plt.title('Boxplot of Columns A and B')<br>
plt.xlabel('Columns')<br>
plt.ylabel('Values')

# Show the plot<br>

plt.show()
This will give you the output:

boxplot with Pandas

38. How do you set an index to a Pandas DataFrame?
Setting an index in a Pandas DataFrame can be done using the “set_index()” method. This allows you to set one or more columns as the index of the DataFrame. Here’s how you can do it:

Changing Index column: In this example, the First Name column has been made the index column of DataFrame.

import pandas as pd<br>

# Create a DataFrame with sample data<br>

data = {'ID': [1, 2, 3, 4, 5],<br>
'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],<br>
'Age': [25, 30, 35, 40, 45]}<br>
df = pd.DataFrame(data)

# Set the 'ID' column as the index<br>

df.set_index('ID', inplace=True)<br>
print(df)
Output:

setting an index to a Pandas DataFrame

Set Index Using Multiple Columns: Two columns will be created as index columns in this example. The append option is used to append given columns to the already existing index column, while the drop parameter is used to drop the column.

import pandas as pd<br>

# Create a DataFrame with sample data<br>

data = {'Country': ['USA', 'Canada', 'USA', 'Canada', 'USA'],<br>
'City': ['New York', 'Toronto', 'Chicago', 'Vancouver', 'Los Angeles'],<br>
'Population': [8000000, 2800000, 2700000, 630000, 4000000]}<br>
df = pd.DataFrame(data)

# Set both 'Country' and 'City' columns as the index<br>

df.set_index(['Country', 'City'], inplace=True)<br>
print(df)
Output of Set Index Using Multiple Columns

39. How do you check and remove duplicate values in Pandas?
In Pandas, duplicate values can be checked by using the duplicated() method.

DataFrame.duplicated()

Here’s an example code:

import pandas as pd<br>

# Create a DataFrame with duplicate values<br>

data = {'Name': ['Alice', 'Bob', 'Charlie', 'Bob', 'Eva'],<br>
'Age': [25, 30, 35, 30, 45]}<br>
df = pd.DataFrame(data)

# Check for duplicate rows<br>

duplicates = df.duplicated()<br>
print(duplicates)
Output:

check and remove duplicate values in Pandas

To remove the duplicate values, we can use the drop_duplicates() method.

DataFrame.drop_duplicates()

Here’s an example code:

import pandas as pd<br>

# Create a DataFrame with duplicate values<br>

data = {'Name': ['Alice', 'Bob', 'Charlie', 'Bob', 'Eva'],<br>
'Age': [25, 30, 35, 30, 45]}<br>
df = pd.DataFrame(data)

# Remove duplicate rows<br>

df_unique = df.drop_duplicates()<br>
print(df_unique)
Output:

Removing Duplicates in Pandas

40. Show two different ways to filter data.
Filtering data in Pandas involves extracting subsets of a DataFrame that meet certain conditions. This is essential for data analysis, allowing focus on relevant data points. Two common methods to filter data in Pandas are Boolean indexing and the query() method.

Boolean Indexing:

Concept: Boolean indexing uses conditional expressions to create a boolean array (True/False) that is applied to the DataFrame. Rows where the condition is “True” are included in the output.
Usage: It’s used for simple and complex conditions, such as filtering rows where column values meet certain criteria.
Example: Filtering rows where a column value is greater than a specified threshold or where multiple conditions are met simultaneously.
Query Method:

Concept: The “query()” method allows filtering using a query string, making it more readable, especially for complex conditions. It uses a string expression to filter data.
Usage: It is particularly useful for more readable syntax and complex filtering conditions, utilizing Python’s eval() to interpret the query string.
Example: Filtering rows where a column value meets a specified condition or combining multiple conditions using logical operators within a string query.
41. How do you add a row to a Pandas DataFrame?
Adding a row to a Pandas DataFrame can be done using several methods. Here are two common ways to achieve this:

Method 1: Using “loc” or “iloc”: You can use the “loc” or “iloc” indexers to add a new row by specifying the index and the row data. Here’s an example code:

import pandas as pd<br>

# Create a DataFrame<br>

data = {'Name': ['Alice', 'Bob'],<br>
'Age': [25, 30]}<br>
df = pd.DataFrame(data)

# New row data<br>

new_row = {'Name': 'Charlie', 'Age': 35}

# Add the new row using loc<br>

df.loc[len(df)] = new_row<br>
print(df)
Method 2: Using “append()”: You can use the “append()” method to add a new row to the DataFrame. Note that it will return a new DataFrame with the row added, so you need to reassign it to the original DataFrame. Here’s an example code:

import pandas as pd<br>

# Create a DataFrame<br>

data = {'Name': ['Alice', 'Bob'],<br>
'Age': [25, 30]}<br>
df = pd.DataFrame(data)

# New row data<br>

new_row = {'Name': 'Charlie', 'Age': 35}

# Add the new row using the append<br>

df = df.append(new_row, ignore_index=True)<br>
print(df)
Pandas and Numpy Interview Questions
42. How do you handle missing data in Pandas?
Handling missing data effectively ensures robust data analysis and modeling, reducing the risk of biased or invalid results. Here are some methods to handle missing data in Pandas.

Detecting Missing Data:
Use isnull() to detect missing values, which returns a DataFrame of the same shape with boolean values indicating missing entries.
Use isnull().sum() to count missing values per column.
Removing Missing Data:
Use dropna() to remove rows or columns with missing values. You can specify axis and subset parameters to control this behavior.
Imputing Missing Data:
Use fillna() to fill missing values with a specified constant, mean, median, mode, or other aggregations.
Interpolating Missing Data:
Use interpolate() to estimate missing values using interpolation methods like linear, polynomial, etc.
43. What is resampling?
Resampling in Pandas refers to the process of converting time series data from one frequency to another. This can involve both upsampling (increasing the frequency of the data) and downsampling (decreasing the frequency of the data). Resampling is commonly used in time series analysis to aggregate data, fill in missing values, or transform the data into a more suitable format for analysis.

Key Concepts of Resampling:

1. Upsampling:

Definition: Increasing the frequency of the time series data (e.g., from daily to hourly).
Usage: Often requires filling or interpolating missing data points that arise due to the increased frequency.
Example: Converting daily data to hourly data.
2. Downsampling:

Definition: Decreasing the frequency of the time series data (e.g., from hourly to daily).
Usage: Involves aggregating data points (e.g., summing, averaging) to match the lower frequency.
Example: Converting hourly data to daily data.
Common Methods for Resampling:

Resample: The resample() method is used to specify a new frequency and apply an aggregation function.
Asfreq: The asfreq() method is used to change the frequency without applying any aggregation, typically used for upsampling.
44. How do you create Timedelta objects in Pandas?
To create a “Timedelta” object using a string, you pass a string literal that specifies the duration.

Example Code:

import pandas as pd

# Convert a string format to a Timedelta object<br>

print(pd.Timedelta('20 days 12 hours 45 minutes 3 seconds'))
Output: 20 days 12:45:03

To create a “Timedelta” object using an integer, simply pass the integer value along with the unit of time.

Example Code:

import pandas as pd<br>

# Convert an integer to a Timedelta object<br>

print(pd.Timedelta(16, unit='h')) # 'h' stands for hours
Output: 0 days 16:00:00

45. How can you Merge Two DataFrames?
The “.merge()” method, which takes two DataFrames as parameters, allows us to combine two DataFrames.

import pandas as pd<br>

# Create two DataFrames<br>

df1 = pd.DataFrame({'A': [1, 2, 3],<br>
'B': [4, 5, 6]},<br>
index=[10, 20, 30])
df2 = pd.DataFrame({'C': [7, 8, 9],<br>
'D': [10, 11, 12]},<br>
index=[20, 30, 40])

# Merge both dataframe<br>

result = pd.merge(df1, df2, left_index=True, right_index=True)<br>
print(result)
Output:

Output of Merging Two DataFrames

46. What does rolling mean?
The rolling mean, also known as the moving average, is a statistical technique used to analyze time series data. It involves calculating the average of a fixed number of sequential data points in a time series. This “rolling” process involves moving the window of fixed size across the data set and recalculating the mean for each position of the window.

Purpose of Rolling Mean:

Smoothing Data: It helps reduce noise and short-term fluctuations, making the underlying trend more visible.
Trend Analysis: By smoothing the data, it becomes easier to identify long-term trends and patterns.
Seasonality Detection: It assists in recognizing seasonal variations by highlighting the cyclical behavior of the data.
Parameters of Rolling Mean:

Window Size: The number of data points included in each calculation of the mean.
Min Periods: The minimum number of observations required to calculate a mean for the window, allowing for handling of missing data.
Characteristics:

NaN Values: The initial calculations may result in `NaN` values due to insufficient data points to fill the window.
Adjustability: The window size and minimum periods can be adjusted to suit the specific characteristics of the data being analyzed.
The rolling mean is widely used in various fields, such as finance for stock price analysis, meteorology for temperature data, and any domain involving time series data to reveal important patterns and trends.

47. How can we convert a NumPy array into a DataFrame?
To convert a NumPy array into a Pandas DataFrame, you can use the pd.DataFrame() constructor. This allows you to specify the data, along with optional arguments such as column names and index labels. Here’s an example code:

import numpy as np<br>
import pandas as pd

# Creating a NumPy array<br>

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Converting NumPy array to DataFrame<br>

df = pd.DataFrame(array, columns=['A', 'B', 'C'])<br>
print(df)
Output:

convert a NumPy array into a DataFrame

48. How can we get the frequency count of unique items in a Pandas DataFrame?
To get the frequency count of unique items in a Pandas DataFrame, you can use the value_counts() method. This method is typically applied to a specific column of the DataFrame to count the occurrences of each unique value.

import pandas as pd

# Creating a sample DataFrame<br>

df = pd.DataFrame({<br>
'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'C', 'B']<br>
})

# Getting the frequency count of unique items in the 'Category' column<br>

frequency_count = df['Category'].value_counts()<br>
print(frequency_count)
Output:

frequency count of unique items in a Pandas DataFrame

49. What do describe() percentiles values represent?
The describe() method in Pandas generates descriptive statistics for the DataFrame columns. The percentile values represent specific points in the data distribution. Percentile values typically include:

50% (median): The middle value separates the higher half from the lower half of the data set.
25% (first quartile): The value below which 25% of the data falls.
75% (third quartile): The value below which 75% of the data falls.
50. Explain data operations in Pandas.
Data operations in Pandas are a set of functions and methods that allow for efficient data manipulation and analysis. Some common operations include:

Selection and Indexing: Accessing data using labels, positions, or a boolean array. Examples include df.loc[], df.iloc[], and direct column access df[‘column’].
Filtering: Extracting subsets of data based on conditions. This can be done using boolean indexing.
Aggregation and Grouping: Summarizing data using functions like sum(), mean(), count(), often combined with groupby().
Merging and Joining: Combining multiple DataFrames using merge(), join(), and concatenation with concat().
Reshaping: Changing the structure of DataFrames with methods like pivot(), melt(), and stack()/unstack().
Handling Missing Data: Managing NaN values using methods like fillna(), dropna(), and isna().
51. What is vectorization in Pandas?
Vectorization in Pandas refers to performing operations on entire arrays or DataFrames without using explicit loops. This approach leverages optimized, low-level implementations to achieve higher performance and efficiency.

Benefits of Vectorization:

Performance: Vectorized operations are much faster than using Python loops.
Simplicity: Code is more concise and easier to read.
52. How will you combine different Data Frames in Panda?
Combining DataFrames in Pandas can be done using several methods:

A. Concatenation: Stacking DataFrames either vertically or horizontally using concat().

df_combined = pd.concat([df1, df2], axis=0)  # Vertical concatenation
df_combined = pd.concat([df1, df2], axis=1)  # Horizontal concatenation
B. Merge: Combining DataFrames based on common columns or indices using merge(). This can perform inner, outer, left, and right joins.

df_merged = pd.merge(df1, df2, on=’key’)
C. Join: Combining DataFrames based on their index using `join()`. This is similar to merge but more index-oriented.

df_joined = df1.join(df2, on=’key’)
For example:

import pandas as pd<br>

# Creating sample DataFrames<br>

df1 = pd.DataFrame({<br>
'ID': [1, 2, 3],<br>
'Value1': ['A', 'B', 'C']<br>
})
df2 = pd.DataFrame({<br>
'ID': [3, 4, 5],<br>
'Value2': ['X', 'Y', 'Z']<br>
})

# Merging DataFrames<br>

df_combined = pd.merge(df1, df2, on='ID', how='outer')<br>
print(df_combined)
