# Mini Project Challenge

## 1. Clean the Customer Data 🏁

💼 Scenario:
You work as a Data Analyst Intern at a retail company. You’ve received messy customer data with missing values. Your job is to clean the data so the marketing team can use it for campaign targeting.

📄 Sample Data:

```python
import pandas as pd

data = {
    'CustomerID': [1001, 1002, 1003, 1004, 1005],
    'Name': ['Alice', None, 'Charlie', 'David', None],
    'Age': [25, None, 29, None, 35],
    'Email': ['alice@gmail.com', 'bob@gmail.com', None, 'david@gmail.com', 'eve@gmail.com'],
    'City': ['New York', 'London', 'Paris', None, 'Berlin']
}

df = pd.DataFrame(data)
print("Original Data:\n", df)
```

🎯 Your Tasks:

1. Identify how many missing values are in each column.

2. Drop rows where both Name and Email are missing.

3. Fill:

    - Name with "Unknown"
    - City with "Not Provided"
    - Age with the median age
    - Email with "<noemail@company.com>"

4. Show the final cleaned DataFrame.

💡 Bonus Task (Optional):
Add a new column "IsAdult":

- True if Age >= 18
- False otherwise

----
Ans

🔍 1. Identify Missing Values

```python
print("\n🔍 Missing values per column:\n", df.isnull().sum())
```

```go
CustomerID    0
Name          2
Age           2
Email         1
City          1
dtype: int64
```

🧹 2. Drop rows where both Name and Email are missing

```python
df = df[~(df['Name'].isnull() & df['Email'].isnull())]
```

In Pandas, the ~ symbol is a bitwise NOT operator.

It is commonly used to invert a boolean mask — in other words, it flips True to False, and False to True.

📌 Use Case in Pandas: Filtering Rows
When filtering rows in a DataFrame, you often write:

```python
df[condition]
```

But if you want the opposite (i.e., rows where the condition is not true), you use:

```py
df[~condition]
```

```import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', None, 'Bob'],
    'Email': ['alice@gmail.com', None, 'bob@gmail.com']
})

# Condition: rows where both Name and Email are missing
condition = df['Name'].isnull() & df['Email'].isnull()

# Invert it: keep rows where NOT both Name and Email are missing
filtered_df = df[~condition]
```

🔄 ~condition means:

> "Select rows where NOT both Name and Email are null"

🛠 3. Fill Missing Values
```python
# Fill Name with "Unknown"
df['Name'].fillna('Unknown', inplace=True)

# Fill City with "Not Provided"
df['City'].fillna('Not Provided', inplace=True)

# Fill Email with generic email
df['Email'].fillna('noemail@company.com', inplace=True)

# Fill Age with median
median_age = df['Age'].median()
df['Age'].fillna(median_age, inplace=True)
```

🆕 4. Add "IsAdult" Column
```python
df['IsAdult'] = df['Age'] >= 18
```

🧾 ✅ Final Cleaned DataFrame:
```python
print("\n✅ Final Cleaned DataFrame:\n", df)
```

Output:

```sql
   CustomerID     Name   Age               Email           City  IsAdult
0        1001    Alice  25.0     alice@gmail.com       New York     True
1        1002   Unknown 29.0       bob@gmail.com       London       True
2        1003  Charlie  29.0  noemail@company.com      Paris        True
3        1004    David  29.0     david@gmail.com       Not Provided True
4        1005   Unknown 35.0       eve@gmail.com       Berlin       True
```

