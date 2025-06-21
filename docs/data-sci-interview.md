# Data Science

## 📊 Pandas / NumPy

### Q1. What are DataFrames in Pandas?

A 2D labeled data structure (like a table in Excel or SQL).

```py
import pandas as pd
data = {'name': ['Ashish', 'Bindra'], 'age': [25, 30]}
df = pd.DataFrame(data)
```

    sno  name  age
    0  Ashish   25
    1  Bindra   30

### Q2. Difference between .loc[] and .iloc[]?

.loc[] is label-based: df.loc[0, 'name']

.iloc[] is index-based: df.iloc[0, 0]

```py
import pandas as pd

# Step 1: Create the DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'London', 'Paris']
}

df = pd.DataFrame(data)
print(df)
```

        Name   Age    City
    0  Alice   24  New York
    1  Bob     27    London
    2  Charlie 22     Paris

🔍 Step 2: Select the second row

```py
second_row_iloc = df.iloc[1]
print("Using iloc:\n", second_row_iloc)
```

📌 Using .loc[] (label-based):

```py
second_row_loc = df.loc[1]
print("Using loc:\n", second_row_loc)
```

Both will give:

```pgsql
Name     Bob
Age        27
City   London
Name: 1, dtype: object
```

🧠 Note:

- .iloc[1] means: “give me the row at position 1” (Python is 0-indexed).

- .loc[1] means: “give me the row with label/index 1”. In this example, labels are default (0,1,2), so .loc[1] and .iloc[1] behave the same.

```py
import pandas as pd

# Step 1: Create the DataFrame with custom labels
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'London', 'Paris']
}

labels = ['a', 'b', 'c']  # custom row labels
df = pd.DataFrame(data, index=labels)
print(df)

```

```css
    Name  Age      City
a  Alice   24  New York
b    Bob   27    London
c Charlie   22     Paris
```

🔍 Step 2: Select the second row
📌 Using .iloc[1] (index-based):

```python
second_row_iloc = df.iloc[1]
print("Using iloc:\n", second_row_iloc)
```

📌 Using .loc['b'] (label-based):

```python
second_row_loc = df.loc['b']
print("Using loc:\n", second_row_loc)
```

### 4. How do you handle missing values in Pandas?

df.dropna()           # Remove rows with NaN  
df.fillna(0)          # Replace NaN with 0

### 5. What is a lambda function in Python?

A small anonymous function defined with lambda keyword.
Example:

```py
 lambda x: x + 1
```

A **lambda function** in Python is a small, anonymous function defined with the keyword `lambda`. It can have any number of input parameters but only one expression. The expression is evaluated and returned when the lambda function is called.

#### Key points

- **Anonymous:** It doesn't need a name.
- **Single expression:** Only one expression, no statements.
- **Used for short functions:** Often used where a simple function is required temporarily.

#### Syntax

```python
lambda arguments: expression
```

#### Example

```python
# Regular function
def add(x, y):
    return x + y

# Lambda equivalent
add_lambda = lambda x, y: x + y

print(add_lambda(3, 5))  # Output: 8
```

#### Typical use cases

- As an argument to functions like `map()`, `filter()`, `sorted()`.
- When you need a quick, throwaway function without formally defining one.

---

Great! Here are some practical examples showing how lambda functions are used in Python:

---

#### 1. Using `lambda` with `map()`

`map()` applies a function to every item of an iterable (like a list).

```python
numbers = [1, 2, 3, 4, 5]

# Multiply each number by 2 using lambda
doubled = list(map(lambda x: x * 2, numbers))

print(doubled)  # Output: [2, 4, 6, 8, 10]
```

---

#### 2. Using `lambda` with `filter()`

`filter()` returns elements for which the function returns True.

```python
numbers = [1, 2, 3, 4, 5, 6]

# Get only even numbers using lambda
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(evens)  # Output: [2, 4, 6]
```

---

#### 3. Using `lambda` with `sorted()`

You can sort complex objects by a specific key with `lambda`.

```python
students = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 78}
]

# Sort students by their score
sorted_students = sorted(students, key=lambda s: s['score'])

print(sorted_students)
# Output: [{'name': 'Charlie', 'score': 78}, {'name': 'Alice', 'score': 85}, {'name': 'Bob', 'score': 92}]
```

---

#### 4. Simple lambda function usage

You can define and call a lambda function directly without assigning it to a variable:

```python
result = (lambda x, y: x ** y)(2, 3)  # 2 raised to the power 3

print(result)  # Output: 8
```

### 6. What is the purpose of train/test split?

To separate data for training and evaluating the model to prevent overfitting.

```python
from sklearn.model_selection import train_test_split
```

The train/test split is a fundamental technique used in machine learning to evaluate how well a model generalizes to unseen data. The idea is to divide the available dataset into two parts:

The training set, which is used to train the model — meaning the model learns the patterns, features, and relationships from this data.

The test set, which is used only after the training is complete, to test how well the model performs on new, unseen data.

This helps in identifying whether the model is overfitting — that is, performing well on training data but poorly on new data — or if it’s generalizing well to different scenarios.

A common practice is to split the data into 80% for training and 20% for testing, but this can vary depending on the size and nature of the dataset.

#### Here’s a quick example using the Iris dataset with a Random Forest classifier

```py
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split dataset: 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
print("Test Accuracy:", accuracy)
```

✅ Why It’s Important

1. Prevents Overfitting:

    - If you test on the same data you train on, the model may just memorize it, not truly learn.

2. Measures Generalization:

    - The test set simulates real-world data. A model that performs well here is more likely to work well in practice.

3. Helps Compare Models:

    - You can evaluate and compare different models or tuning methods objectively using the same test data.

🔹 Typical Split Ratios

- 80/20 or 70/30:

  - 80% for training, 20% for testing.

- 60/20/20 (with validation):

  - Used when a separate validation set is needed during training for tuning hyperparameters.

### 7. What is overfitting?

When a model performs well on training data but poorly on unseen/test data.

### 8. What is overfitting and how do you prevent it?

When a model performs well on training data but poorly on unseen data. Prevent using:

1. Cross-validation
2. Regularization
3. Simpler models
4. More training data

### 9. Name a few machine learning algorithms

1. Linear Regression
2. Decision Tree
3. K-Nearest Neighbors
4. Logistic Regression
5. Random Forest

### 10. What is a confusion matrix?

A table showing true positives, false positives, true negatives, and false negatives. Helps evaluate classification models.

### 11. How would you visualize a correlation between numeric columns?

```py
import seaborn as sns
sns.heatmap(df.corr(), annot=True)

```

### 12. You have a CSV with 1M rows. How would you load it efficiently?

```py
df = pd.read_csv('large_file.csv', chunksize=100000)  # Load in parts
```

preview first few rows:

```py
df = pd.read_csv('large_file.csv', nrows=1000)
```

## Data Analysus

### 1. What is data analysis?

Data analysis is the process of inspecting, cleaning, transforming, and modeling data to find useful information and support decision-making.

### 2. What steps do you take when cleaning a dataset?

- Remove duplicates
- Handle missing values (dropna() or fillna())
- Fix incorrect data types
- Normalize or standardize if needed
- Rename inconsistent column names

### 3. How do you handle missing data?

- Remove rows (dropna())
- Fill with mean/median/mode (fillna())
- Use interpolation or predictive models

### 4. What is the difference between correlation and causation?

Correlation: A relationship between two variables.

Causation: One variable causes the change in another.

### 5. What is the purpose of a GROUP BY clause in SQL?

It groups rows that have the same values into summary rows like SUM, AVG, COUNT.

### 6. How do you visualize categorical vs numerical data?

Categorical: Bar chart, Pie chart

Numerical: Histogram, Box plot, Line plot

### 7. How would you find duplicate rows in a dataset using Pandas?

```py
duplicates = df[df.duplicated()]
```

### 8. Explain the difference between INNER JOIN and LEFT JOIN

```
INNER JOIN: Returns matching records from both tables.

LEFT JOIN: Returns all records from the left table, and matched ones from the right.
```

### 9. What is an outlier and how can you detect it?

An outlier is a data point that is significantly different from others.
Detected using:

- Box plot
- Z-score
- IQR (Interquartile Range)

### Revenue dropped last month. What would you check?

Answer:

- Compare sales across months
- Check customer churn or drop in high-value orders
- Analyze product-level trends
- Look for marketing or external factors

## Statistics & Probability

### What is the difference between mean, median, and mode?

## ✅ **Difference Between Mean, Median, and Mode**

| Measure            | Definition                                        | Use Case                              | Example                                |
| ------------------ | ------------------------------------------------- | ------------------------------------- | -------------------------------------- |
| **Mean** (Average) | Sum of all values divided by the number of values | Best for normally distributed data    | `(2 + 3 + 4 + 5 + 6) / 5 = 4`          |
| **Median**         | The middle value when data is sorted              | Best when data has outliers           | Sorted `[1, 2, 3, 100] → Median = 2.5` |
| **Mode**           | The value that appears most frequently            | Best for categorical or discrete data | `[1, 2, 2, 3] → Mode = 2`              |

---

### 🔍 Example

Given this list:

```python
data = [1, 2, 2, 3, 100]
```

```python
import statistics as stats

mean = stats.mean(data)     # 21.6
median = stats.median(data) # 2
mode = stats.mode(data)     # 2
```

- **Mean** = 21.6 → pulled up by **100** (an outlier)
- **Median** = 2 → unaffected by extreme values
- **Mode** = 2 → the most frequent number

---

### 🧠 Summary

| Term   | Sensitive to Outliers? |
| ------ | ---------------------- |
| Mean   | ✅ Yes                  |
| Median | ❌ No                   |
| Mode   | ❌ No                   |

---

### What is standard deviation? Why is it important?

### Explain the concept of p-value

### What is correlation vs causation?

## Excel/Pandas/SQL Skills

### How would you find duplicate entries in a dataset using Excel or Pandas?

### Write an SQL query to find the second highest salary from an employee table

### How do you merge two datasets in Pandas?

### What are GROUP BY and HAVING clauses in SQL?

## 🔹 Data Cleaning & Preprocessing

### What steps do you follow for data cleaning?

### How do you handle outliers in a dataset?

### What is data normalization and why is it necessary

## Visualization

### What tools have you used for data visualization?

### When would you use a bar chart vs a pie chart?

### How do you visualize relationships between two numerical variables?

## 🔹 Scenario-Based (Practical Thinking)

### You are given sales data with inconsistent date formats and missing customer IDs. What would be your approach to clean and analyze it?

### If the company’s revenue dropped last quarter, how would you investigate the cause using data?

## 🔹 Behavioral/Soft Skills

### Tell us about a time you worked on a team project with data

### How do you prioritize tasks when working on multiple datasets with tight deadlines?

## Data Science Libraries

### What is NumPy used for in data science?

### How is Pandas useful for data manipulation?

### What are DataFrames in Pandas and how do you create one?

### How would you filter rows in a DataFrame based on a condition?

### What’s the difference between .loc[] and .iloc[] in Pandas?

## 📈 Visualization (Matplotlib/Seaborn)

### How do you create a basic line plot using Matplotlib?

### What types of plots can you create with Seaborn?

### How would you visualize missing values in a dataset?

## 📦 Data Preprocessing & Cleaning

### How do you handle missing values in Pandas?

### What is the difference between dropna() and fillna()?

### How do you normalize or scale numerical data?

### What is one-hot encoding and when do you use it?

## 🔢 Statistics & Machine Learning (Basics)

### ### What is the difference between supervised and unsupervised learning?

### Name a few common algorithms used for classification

### What does train-test split mean and why is it important?

### What is overfitting and how do you prevent it?

### Explain the purpose of cross-validation

### What is a confusion matrix?

## 📁 Project & Scenario-Based

### You have a CSV file with 1 million rows. How would you load and analyze it efficiently in Python?

### If your model accuracy is 95%, what additional metrics would you check?

### Describe a Python project you've worked on (can be academic or personal). What libraries did you use?

Great! Here's a **visual summary + mini challenge** for handling missing data in Pandas.

---

## 📊 **Visual Summary: How to Handle Missing Data**

| 🔧 Method       | 📘 Code Example                              | 💡 When to Use                           |
| --------------- | -------------------------------------------- | ---------------------------------------- |
| Detect Missing  | `df.isnull().sum()`                          | To find how many values are missing      |
| Drop rows       | `df.dropna()`                                | If missing data is minimal               |
| Drop columns    | `df.dropna(axis=1)`                          | If a column has too many missing values  |
| Fill with value | `df.fillna('Unknown')`                       | For categorical columns like 'City'      |
| Fill with mean  | `df['Age'].fillna(df['Age'].mean())`         | For numerical data like age or income    |
| Forward fill    | `df.fillna(method='ffill')`                  | For time series or ordered data          |
| Group-wise fill | `df.groupby('Gender')['Age'].transform(...)` | When filling based on a related category |

---

## 🧪 Mini Challenge

You are given a messy employee dataset:

```python
import pandas as pd

data = {
    'EmployeeID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', None, 'David', 'Eva'],
    'Department': ['Sales', None, 'HR', None, 'IT'],
    'Age': [25, None, 30, None, 35]
}

df = pd.DataFrame(data)
print("Original DataFrame:\n", df)
```

### 🎯 Your Tasks

1. Find the number of missing values in each column.
2. Fill `Name` and `Department` with `"Unknown"`.
3. Fill `Age` with the median age.
4. Print the cleaned DataFrame.

---
