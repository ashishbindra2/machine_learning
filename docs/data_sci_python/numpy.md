https://intellipaat.com/blog/interview-question/numpy-interview-questions/

1. What is Numpy? Why do we use it?
NumPy is a Python library used for numerical computing, especially for handling arrays and matrices. We use it because it provides efficient operations on large datasets and supports mathematical functions essential for scientific computing and data analysis.

2. How can I make an array in NumPy?
You can make an array in NumPy using the numpy.array() function.

For example,

import numpy as np<br>
my_array = np.array([1, 2, 3])
Array in NumPy

3. What are the advantages and disadvantages of Numpy?
Advantages	Disadvantages
Efficient numerical operations	Limited support for non-numeric data types  
Simplified syntax for complex mathematical computations	Memory-intensive for large arrays
Seamless integration with other Python libraries like SciPy and Pandas	Lack of built-in support for distributed computing
Extensive documentation and community support	Steep learning curve for beginners due to its complex syntax and advanced functionalities
4. Why is NumPy better than Yorick, Matlab, Octave, or Idl?
NumPy outperforms Yorick, MATLAB, Octave, and IDL due to its efficient combination of Python and optimized C/C++ code, providing faster numerical computations. It offers a vast library of functions and data structures, seamlessly integrating with the broader Python ecosystem. NumPy’s large and active community ensures better documentation, more third-party packages, and quicker development of new features. As an open-source and cross-platform library, NumPy is free to use and accessible on various operating systems, making it a more versatile and scalable choice for scientific and data-intensive applications.

5. What are ndarrays in NumPy?
Ndarrays are multi-dimensional arrays in NumPy used for efficient numerical computations and data manipulation. They are the main building block of NumPy.

It’s basically a way to store data in tables with multiple dimensions, like spreadsheets. They’re super fast because they’re optimized for math stuff. Once you make one, you can’t change its size, but you can do basic mathematics with it. They only like to store the same type of data, like all numbers or all text.

Get 100% Hike!

Master Most in Demand Skills Now!

Email Address

+91  IN          INDIA
Phone Number
By providing your contact details, you agree to our Terms of Use & Privacy Policy
6. Explain the difference between shallow copy and deep copy in NumPy.
Shallow Copy	Deep Copy
Creates a new object with references to the original data	Creates a completely new and independent object
Changes to the copied object affect the original	Changes to the copied object don’t affect the original
Faster and uses less memory	Slower and uses more memory
Copies only the top-level structure, not the nested objects	Copies of both the top-level structure and nested objects
7. In a NumPy array, how can we access the elements?
In NumPy, we can access an array in two ways. Either by slicing or by indexing. For example:

To access a single element: array[index]
To access a slice of elements: array[start_index:end_index]
For multi-dimensional arrays, you can use comma-separated indices: array[row_index, column_index]
8. What is a var function in NumPy?
In NumPy, the “var” function calculates the variance of elements within an array or across a designated axis. Variance is a measure of the spread or dispersion of a set of data points.

np.var(a, axis=None, dtype=None)

a: The array for which variance computation is desired.

axis: Specifies the axis or axes for variance computation. If not provided, variance is computed for the entire array. It can be an integer or a tuple of integers for multiple axes.

dtype: Defines the data type of the resultant variance. If unspecified, the data type is inferred from the input array.

9. How can you create arrays in NumPy that are 1D, 2D, and 3D?
Let’s say you have a standard Python list. Using the array function, we can generate NumPy arrays in the manner described below:

One dimensional array:

import numpy as np<br>
arr = [1,2,3,4] #python list<br>
numpy_arr = np.array(arr) #numpy array
Two-dimensional arrays:

import numpy as np<br>
arr = [[1,2,3,4],[4,5,6,7]]<br>
numpy_arr = np.array(arr)
Three-dimensional arrays:

import numpy as np<br>
arr = [[[1,2,3,4],[4,5,6,7],[7,8,9,10]]]<br>
numpy_arr = np.array(arr)
10. How can you create a NumPy array from a Python list?
You can create a NumPy array from a Python list using the “numpy.array()” function. Here’s an example:

import numpy as np<br>
# Create a Python list<br>
my_list = [1, 2, 3, 4, 5]<br>
# Convert the list to a NumPy array<br>
my_array = np.array(my_list)<br>
# Print the NumPy array<br>
print(my_array)
This will give you the following output:

[1 2 3 4 5]

11. Which common data types does NumPy support?
NumPy supports several common data types. These data types allow for flexibility in representing different kinds of numerical and non-numerical data in NumPy arrays. These types are:

Common Data Types That NumPy Supports

12. How is NumPy different from Pandas?
NumPy and Pandas are two essential libraries in the Python ecosystem for data manipulation and analysis, but they serve slightly different purposes.

NumPy is primarily focused on numerical computing, providing support for multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently. 

On the other hand, Pandas is built on top of NumPy and provides higher-level data structures, notably the DataFrame, a tabular, spreadsheet-like data structure. Pandas excel in data manipulation, cleaning, and analysis tasks, offering powerful tools for handling missing data, reshaping datasets, grouping, merging, and joining datasets.

13. How do you count the number of times a given value appears in an array of integers?
The number of times a given value appears can be counted using the “bincount()” function. It’s important to remember that the bincount() method accepts two types of arguments: boolean expressions and positive integers. Null values are not permitted to be used. Use the function NumPy.bincount ().
For example,

import numpy as np<br>
arr = np.array([2,3,1,5,0,3,8,1,0,0,3,7,6])<br>
print(np.bincount(arr))
This will give us the following output:

[3 2 1 3 0 1 1 1 1]

14. What is the difference between copy and view?
Copy: When you create a copy of a NumPy array, you get a new array with its own separate data.
Any changes to the copied array won’t affect the original array, and vice versa.
A copy essentially duplicates the data in memory.

import numpy as np<br>
original_array = np.array([1, 2, 3, 4, 5])<br>
copied_array = original_array.copy()<br>
copied_array[0] = 100<br>
print("Original array:", original_array)<br>
print("Copied array:", copied_array)
Output:

Original array: [1 2 3 4 5]
Copied array: [100 2 3 4 5]

View: It is a new array object that refers to the same underlying data as the original array.
Modifications to the view will affect the original array, and vice versa.
Views provide different ways to look at the same data without copying it.

import numpy as np<br>
original_array = np.array([1, 2, 3, 4, 5])<br>
view_array = original_array.view()<br>
view_array[0] = 100<br>
print("Original array:", original_array)<br>
print("View array:", view_array)
Output:

Original array: [100 2 3 4 5]
View array: [100 2 3 4 5]

15. How do you identify the data type of an array?
One can identify the data type of a NumPy array using the “dtype” attribute. Let’s check out the given code to know “how”.

import numpy as np<br>
arr = np.array([1, 2, 3, 4, 5])<br>
data_type = arr.dtype<br>
print("Data type of the array:", data_type)
Output:

Data type of the array: int64

16. How do you create an array with all values as zeros or ones?
For this, we will use the np.zeros() and np.ones() methods.

Creating an array with all zero values:

import numpy as np<br>
zeros_array = np.zeros((3, 3))<br>
print("Array with all zeros:")<br>
print(zeros_array)
Output:

Array with all zeros:
[[0. 0. 0.]
[0. 0. 0.]
[0. 0. 0.]]

Creating an array with all one values:

import numpy as np<br>
ones_array = np.ones((3,3))<br>
print("Array with all ones:")<br>
print(ones_array)
Output:

Array with all ones:
[[1. 1. 1.]
[1. 1. 1.]
[1. 1. 1.]]

17. Display nine random integer numbers from 1 to 50 in an array.
We can generate an array with nine random integer numbers from 1 to 50 using “numpy.random.randint()” function.

import numpy as np<br>
rand_arr = np.random.randint(1,50,size=9)<br>
print (rand_arr)
Output:

[37 6 32 7 31 45 25 16 35]

18. How can you reverse a NumPy array?
We can reverse a NumPy array using slicing. Here’s an example:

import numpy as np<br>
arr = np.array([1, 2, 3, 4, 5])<br>
reversed_arr = arr[::-1] # Reverse the array using slicing<br>
print("Reversed array:")<br>
print(reversed_arr)
Output:

Reversed array:
[5 4 3 2 1]

Another way to reverse a NumPy array is by using the “numpy.flip()” function.

Advanced NumPy Interview Questions
19. How do you check whether an array is empty or contains zero elements?
In NumPy, you can utilize the “size” attribute to determine if an array is empty or has zero elements. This attribute provides the total count of elements in the array. If the size is zero, it signifies that the array is empty or has no elements.












Process Advisors

ey-logo
*Subject to Terms and Condition
20. What is the difference between slicing and indexing in NumPy?
The basic methods for accessing and modifying elements in arrays are indexing and slicing, but some key distinctions must be noted.

Slicing	Indexing
Returns a portion of the original array as a new array	Returns a single element or a subset of elements from the original array
Allows selecting a range of elements using start, stop, and step parameters	Selects a specific element or elements using integer indices
Can create arrays with fewer dimensions than the original array	Can access individual elements or subsets of elements from the original array
Syntax: array[start:stop:step]	Syntax: array[index] or array[row_index, column_index]
Check out our blog on Data Science Tutorial to learn more about Data Science.

21. What is vectorization in NumPy?
Vectorization in NumPy refers to the process of applying operations on entire arrays rather than on individual elements. This is achieved through NumPy’s ability to perform element-wise operations, broadcasting, and other array manipulation techniques efficiently.

When you perform operations on NumPy arrays, the operations are automatically applied element-wise, meaning the operation is executed on each element of the array simultaneously. This can significantly improve computational efficiency compared to using explicit loops to iterate over each element.

For example, consider adding two arrays:

import numpy as np<br>
a = np.array([1, 2, 3, 4])<br>
b = np.array([5, 6, 7, 8])<br>
result = a + b
Output:

[6, 8, 10, 12]

This addition operation is performed element-wise across the entire arrays a and b without the need for explicit looping.

Vectorization is a fundamental concept in NumPy and is key to writing concise, efficient, and readable code for numerical computing tasks. It uses underlying C implementations for array operations, making it much faster than equivalent Python loops.

22. How can the local maxima or peaks in a 1-D NumPy array be found?
You can find the local maxima or peaks in a 1-D NumPy array using various methods. One common approach is to iterate over the array and compare each element with its neighbors to determine whether it’s a peak.

peaks in a 1-D NumPy array

Here’s a basic implementation of this approach:

import numpy as np<br>
def find_peaks(arr):<br>
peaks = []<br>
for i in range(1, len(arr) - 1):<br>
if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:<br>
peaks.append(i)<br>
return peaks
# Example usage:<br>
arr = np.array([1, 3, 7, 2, 5, 8, 4])<br>
peaks = find_peaks(arr)<br>
print("Peaks found at indices:", peaks)<br>
print("Peak values:", arr[peaks])
Output:

Peaks found at indices: [2, 5]
Peak values: [7 8]

This function iterates over the array and checks if each element is greater than its neighboring elements. If so, it considers the element a peak and adds its index to the list of peaks.

23. How do you add matrices using NumPy?
One can simply achieve this using the “+” addition operator. So, first construct two matrices that you want to add. Then perform simple addition between two ndarrays.

import numpy as np<br>
matrix1 = np.array([[1, 2, 3],<br>
[4, 5, 6],<br>
[7, 8, 9]])
matrix2 = np.array([[10, 11, 12],<br>
[13, 14, 15],<br>
[16, 17, 18]])<br>
# Add the matrices<br>
result = matrix1 + matrix2<br>
print(result)
Output:

[[11 13 15]
[17 19 21]
[23 25 27]]

24. How do you multiply matrices using NumPy?
To multiply two matrices, we can use the “np.dot()” function or the “@” operator for Python 3.5. Considering the matrices we created above, let’s perform the multiplication.

np.dot() function:
result = np.dot(matrix1, matrix2)
print(result)

@ operator:
result = matrix1 @ matrix2
print(result)

For both cases, the output would be:

[[ 84 90 96]
[201 216 231]
[318 342 366]]

25. What is array slicing, and how do you do it in NumPy?
Slicing is the process of taking a subset of the provided array and using it to create a new view of it without actually copying it. In NumPy, array slicing is performed using the colon: operator within square brackets [ ]. The syntax for array slicing is start:stop:step, where
start is the starting index (inclusive)
stop is the stopping index (exclusive)
step is the step size, indicating the spacing between elements

For example, take an array [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and consider different cases as shown in the image along with the respective outputs:

Slicing in NumPy

Go through these Data Science Interview Questions and Answers to excel in your interview.

26. Swap two rows/columns in a 2D array.
For swapping in 2D arrays, one can use advanced indexing without the need for temporary variables:

import numpy as np<br>
arr_2d = np.array([[1, 2, 3],<br>
[4, 5, 6],<br>
[7, 8, 9]])<br>
# Swap rows using advanced indexing<br>
arr_2d[[0, 1]] = arr_2d[[1, 0]]<br>
# Swap columns using advanced indexing<br>
arr_2d[:, [0, 1]] = arr_2d[:, [1, 0]]<br>
print(arr_2d)
Output:

[[5 4 6]
[2 1 3]
[8 7 9]]

27. How are vectorization and broadcasting related to each other in NumPy?
Vectorization: Imagine you have a list of numbers, and you want to add 5 to each number in that list. You could write a loop that goes through each number, adds 5 to it, and stores the result. That’s how you’d do it in regular Python.
However, in NumPy, you can do the same thing in one step without any loops. You just tell NumPy to add 5 to the entire list at once. This way, NumPy handles all the individual additions behind the scenes in an optimized way, which is much faster than doing it one by one.

Broadcasting: Let’s say you have two lists of numbers, and you want to add them together. If both lists are the same size, it’s easy; you just add each pair of numbers together. But what if one list has fewer numbers than the other? That’s where broadcasting comes in.
NumPy can automatically stretch or “broadcast” the smaller list to match the size of the larger one, so you can still add them together without any issues. It lets you do that resizing automatically, so you can perform operations on arrays of different sizes without any extra effort.

Vectorization and broadcasting are related in that they both enable efficient and concise array operations in NumPy. Vectorization allows operations to be applied element-wise across entire arrays, eliminating the need for looping in Python. Broadcasting extends this concept by enabling operations between arrays with different shapes, automatically aligning their dimensions to perform element-wise operations seamlessly.

28. In NumPy, how will the moving average for the 1D array be implemented?
In NumPy, you can implement the moving average for a 1D array using convolution. Convolution is a mathematical operation that combines two functions to produce a third function, which represents how one function modifies the shape of the other. In the context of moving averages, you can use a simple kernel (also called a “window” or “filter”) of equal weights to compute the average over a sliding window of elements in the array.

29. What is a masked array in NumPy?
In NumPy, an array that has an additional Boolean mask added to it that designates some entries as invalid or masked is called a masked array. As a result, you can deal with data that contains incorrect or missing numbers without having to change the original data. Masked arrays may be extremely handy, especially when working with real-world datasets that might contain inconsistent or missing data points.

30. How do you sort a NumPy array in ascending or descending order?
You can sort a NumPy array in ascending or descending order using the “np.sort()” function. By default, this function sorts the array in ascending order. If you want to sort the array in descending order, you can use the [::-1] slicing notation to reverse the sorted array. Here’s an example:

import numpy as np<br>
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])<br>
# Sort the array in ascending order<br>
sorted_arr_ascending = np.sort(arr)<br>
print(sorted_arr_ascending)
Output:

[1 1 2 3 3 4 5 5 6 9]

In descending order:

import numpy as np<br>
arr = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])<br>
# Sort the array in descending order<br>
sorted_arr_descending = np.sort(arr)[::-1]<br>
print(sorted_arr_descending)
Output:

[9 6 5 5 4 3 3 2 1 1]

31. What happens if we split the NumPy array using the arrays_split() method?
The np.array_split() function in NumPy is used to split a NumPy array into multiple sub-arrays along a specified axis. It takes two arguments: the original array and the number of sub-arrays to create. The function returns a list of the split sub-arrays, with the length of the list equal to the number of sections specified.

import numpy as np<br>
# Create a sample NumPy array<br>
original_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])<br>
# Split the array into 3 sub-arrays<br>
split_arrays = np.array_split(original_array, 3)<br>
# Print the results<br>
print("Original Array:", original_array)<br>
print("Split Arrays:")<br>
for sub_array in split_arrays:<br>
print(sub_array)
Output:

Original Array: [ 1 2 3 4 5 6 7 8 9 10]
Split Arrays:
[1 2 3 4]
[5 6 7]
[ 8 9 10]

32. How do you convert a Pandas DataFrame into a NumPy array?
Converting a Pandas DataFrame into a NumPy array can be done using the .to_numpy() method. This method is straightforward and efficient, and it allows you to convert the entire DataFrame or a subset of it into a NumPy array. For example:

import pandas as pd<br>
import numpy as np<br>
# Create a sample DataFrame<br>
data = {<br>
'A': [1, 2, 3],<br>
'B': [4, 5, 6],<br>
'C': [7, 8, 9]<br>
}<br>
df = pd.DataFrame(data)<br>
# Convert the DataFrame to a NumPy array<br>
numpy_array = df.to_numpy()<br>
print(numpy_array)
Output:

[[1 4 7]
[2 5 8]
[3 6 9]]

33. How can you randomly shuffle the elements of a NumPy array?
You can use the numpy.random.shuffle function to randomly shuffle the elements of a NumPy array.

import numpy as np<br>
my_array = np.array ([7,9,12,5,2,8])<br>
np.random.shuffle(my_array)<br>
print (my_array)
Output:

[ 8 12 9 2 7 5]

34. How do you remove missing or null values from a NumPy array?
One can accomplish this by employing a masked array or a boolean mask to filter out missing or null data. For example:

import numpy as np<br>
# Create a NumPy array with missing values (NaN)<br>
arr = np.array([10, 20, np.nan, 40, 50])<br>
# Create a masked array where missing values are masked<br>
masked_arr = np.ma.masked_invalid(arr)<br>
# Access only non-missing values<br>
clean_data = masked_arr.compressed()<br>
print(clean_data)
Output:

[10. 20. 40. 50.]

35. Which methods are frequently used to normalize data in a NumPy array?
Normalization of data in a NumPy array is a crucial preprocessing step in many machine learning and data analysis tasks. Normalization ensures that all features have the same scale, which can improve the performance of machine learning algorithms, particularly those sensitive to feature scaling, such as gradient descent-based optimization algorithms. Some commonly used methods for normalizing data in a NumPy array are:

Min-Max Scaling
Z-Score Normalization (Standardization)
Log Transformation
Box-Cox Transformation
Robust Scaling
36. How is fliplr different from flipud methods in NumPy?
An array can be flipped left or right using the fliplr() function. Although the columns remain unchanged, the pieces within them are arranged differently than they were previously. The following graphic serves as an illustration of this:

fliplr method in NumPy

It is clear that in the final product, the element placements are reversed from their initial positions to the left or right.

Syntax:
np.fliplr(arr)
where the array that has to be flipped is denoted by arr.

The array can also be flipped up or down using the flipud function. In this case, the rows are retained, but the final result may show them in a different order. The picture below illustrates this:

flipud method in NumPy

Here, we can observe that the elements with the digits 1, 3, and 5 are inverted in the outcome.

Syntax:
np.flipud(arr)
where the array that has to be flipped is arr

37. Discuss the role of NumPy in feature engineering for machine learning.
NumPy, the fundamental package for scientific computing with Python, plays a pivotal role in feature engineering for machine learning. Its multidimensional arrays enable easy storage and manipulation of datasets, facilitating preprocessing tasks such as scaling, normalization, and transformation. 

In feature engineering, NumPy empowers practitioners to create new features by combining existing ones, extracting meaningful information, or encoding categorical variables. Its broadcasting and vectorized operations accelerate computations, enhancing the scalability of feature engineering pipelines. Additionally, NumPy seamlessly integrates with other machine learning frameworks like sci-kit-learn, enabling smooth data flow from feature engineering to model training and evaluation. 

Overall, NumPy’s speed, versatility, and compatibility make it an indispensable tool for crafting informative features that contribute to the performance and interpretability of machine learning models.

Pandas and Numpy Interview Questions
38. What is the difference between using the shape and size attributes of a NumPy array?
The shape and size attributes of a NumPy array provide different kinds of information about the array. The shape tells you the structure of the array (its dimensions), whereas the size tells you how many elements are there in total.

Shape: The shape attribute returns a tuple that represents the dimensions of the array. For example, if you have a 2D array with 3 rows and 4 columns, the shape tuple would be (3, 4). It tells you the number of elements in each dimension of the array.

Size: The size attribute returns the total number of elements in the array. It essentially gives you the count of all the elements in the array, regardless of their dimensions. For example, if you have a 2D array with shape (3, 4), the size would be 3 * 4 = 12.

39. In what ways does NumPy incorporate well-known machine learning frameworks?
NumPy serves as the foundational library for numerical computing in Python, playing a pivotal role in various machine learning frameworks due to its efficient array operations and mathematical functions. Here are some ways NumPy integrates into well-known machine learning frameworks:

Data Representation: NumPy arrays serve as the standard data format in frameworks like TensorFlow and PyTorch.
Matrix Operations: Its efficient array operations power matrix computations, foundational for algorithms in sci-kit-learn.
Integration: NumPy seamlessly integrates with SciPy, Pandas, and Matplotlib for preprocessing, visualization, and analysis.
Performance: Optimized core routines in C and Fortran accelerate computations, crucial for large datasets and complex models.
Customization: NumPy’s flexibility allows for easy implementation of custom operations, enhancing framework extensibility.
Ease of Use: Intuitive syntax and extensive documentation make NumPy accessible to novice and expert users, facilitating smooth integration into machine learning workflows.
40. What is the purpose of the np.frompyfunc() function? How is it different from a ufunc?
“np.frompyfunc()” is a function in NumPy that creates a universal function (ufunc) from an arbitrary Python function. The purpose is to provide a way to vectorize (apply element-wise) a Python function across NumPy arrays, allowing for efficient element-wise operations without the need for explicit looping.

Here’s a breakdown of its purpose and differences compared to a ufunc:

Purpose

np.frompyfunc(): It is used to create a ufunc from a Python function. This is particularly useful when you have a custom Python function that you want to apply element-wise to NumPy arrays.
ufunc: Ufuncs are functions that operate element-wise on NumPy arrays, providing efficient and vectorized computations. They are already implemented for many mathematical operations and built-in functions in NumPy.
Input and Output

np.frompyfunc(): Takes a Python function as input and returns a ufunc object.
ufunc: Operates directly on NumPy arrays as input and produces NumPy arrays as output.
Performance

np.frompyfunc(): Although it creates a ufunc, the performance might not be as efficient as native ufuncs because the underlying function is still implemented in Python.
ufunc: Native ufuncs are implemented in compiled C code, offering optimized performance for element-wise operations on arrays.
Usage

np.frompyfunc(): Useful when you have a custom Python function that you want to use with NumPy arrays but it’s not natively supported as a ufunc.
ufunc: Preferable for standard mathematical operations and built-in functions where native ufuncs are available for efficient computation.
41. Explain the concept of strides in NumPy. How are they related to array memory layout and performance?
In NumPy, strides are a tuple of integers that describe the step size in bytes to move from one element to the next in each dimension of an array. They are crucial for understanding the array’s memory layout and accessing elements efficiently.

Consider a 2D array. The strides determine how many bytes you need to skip to move to the next element in each dimension. For example, in a 2D array with shape (3, 4) and element type float32 (4 bytes), the strides might be (16, 4). This means to move to the next row, you skip 16 bytes (4 elements * 4 bytes each), and to move to the next column within a row, you skip 4 bytes.

Strides are tightly connected to the array’s memory layout:

C-contiguous layout: The last dimension has the smallest stride, and elements in the same row are contiguous in memory.
F-contiguous (Fortran) layout: The first dimension has the smallest stride, and elements in the same column are contiguous in memory.
Strides affect performance due to memory access patterns:

Cache efficiency: Accessing contiguous memory locations (like in C-contiguous arrays) is faster due to better cache utilization.
Element-wise operations: Efficient strides can minimize the number of memory jumps, enhancing performance.
42. Explain how you can use NumPy to perform Fourier transformations.
NumPy’s “numpy.fft” module provides essential functions for performing Fourier transformations, which are used to convert signals between the time and frequency domains:

1D Fourier Transform

Forward Transform: The numpy.fft.fft function computes the discrete Fourier Transform (DFT) of a one-dimensional array.
Inverse Transform: The numpy.fft.ifft function computes the inverse DFT, transforming the frequency domain back to the time domain.
2D Fourier Transform

Forward Transform: The numpy.fft.fft2 function computes the two-dimensional DFT, commonly used for image processing.
Inverse Transform: The numpy.fft.ifft2 function computes the inverse two-dimensional DFT.
Real-Valued Signals

Forward Transform: The numpy.fft.rfft function is optimized for computing the DFT of real-valued signals, leveraging their properties to reduce computation time and storage.
Inverse Transform: The numpy.fft.irfft function computes the inverse DFT for real-valued signals, returning the signal to the time domain.
These Fourier transform functions enable efficient signal and image analysis by allowing manipulation in the frequency domain, such as filtering and spectral analysis.

43. What is the difference between hstack() and vstack() in NumPy?
Function	Description	Axis of Concatenation	Example
hstack()	Stack arrays horizontally (side by side)	Second axis (axis 1)	If arrays have the same number of rows, they are concatenated horizontally.
vstack()	Stack arrays vertically (on top of each other)	First axis (axis 0)	If arrays have the same number of columns, they are concatenated vertically.
44. How do you extract the diagonal elements of a square 2D NumPy array matrix?
To extract the diagonal elements of a square 2D NumPy array matrix, you can use the np.diagonal() function. Here’s an example:

import numpy as np<br>
# Create a square 2D NumPy array matrix<br>
matrix = np.array([[1, 2, 3],<br>
[4, 5, 6],<br>
[7, 8, 9]])<br>
# Extract the diagonal elements<br>
diagonal_elements = np.diagonal(matrix)<br>
print(diagonal_elements)
Output:

[1 5 9]

45. Create a program that takes a string element and changes it to the capitalization of the initial letter, lowercase, title-case, swapcase, and uppercase of a given NumPy array.
One can achieve this using NumPy’s vectorized string operations. Here’s a Python program that demonstrates this:

import numpy as np<br>
# Create Sample NumPy array<br>
arr = np.array(['Intellipaat', 'Software', 'Solutions'], dtype=str)
upper_case_arr = np.char.upper(arr)<br>
lower_case_arr = np.char.lower(arr)<br>
capitalize_case_arr = np.char.capitalize(arr)<br>
titlecase_arr = np.char.title(arr)<br>
swapcase_arr = np.char.swapcase(arr)
print("Upper Conversion: ", upper_case_arr)<br>
print("Lower Conversion: ", lower_case_arr)<br>
print("Capitalize First Letter Conversion: ", capitalize_case_arr)<br>
print("Titlecase Conversion: ", titlecase_arr)<br>
print("Swapcase Conversion: ", swapcase_arr)
Output:

Upper Conversion: [‘INTELLIPAAT’ ‘SOFTWARE’ ‘SOLUTIONS’]
Lower Conversion: [‘intellipaat’ ‘software’ ‘solutions’]
Capitalize First Letter Conversion: [‘Intellipaat’ ‘Software’ ‘Solutions’]
Titlecase Conversion: [‘Intellipaat’ ‘Software’ ‘Solutions’]
Swapcase Conversion: [‘iNTELLIPAAT’ ‘sOFTWARE’ ‘sOLUTIONS’]

46. Create a program that adds spaces to each character in every NumPy array entry.
Here’s an example code:

import numpy as np<br>
def add_spaces_to_array(arr):<br>
# Convert the array to string type<br>
arr = arr.astype(str)<br>
# Add spaces to each character<br>
spaced_array = np.char.add(arr, ' ')<br>
return spaced_array<br>
# Example usage<br>
array = np.array(["Intellipaat", "Software", "Solutions"])<br>
spaced_array = add_spaces_to_array(array)<br>
print(spaced_array)
Output:

[‘Intellipaat ‘ ‘Software ‘ ‘Solutions ‘]

47. Make a 3 * 3 matrix with values from 1 to 9.
You can create a 3×3 matrix with values from 1 to 9 using NumPy’s arange() function to generate the values and then reshape it into a 3×3 matrix. Here’s how you can do it:

import numpy as np<br>
# Generate values from 1 to 9<br>
values = np.arange(1, 10)<br>
# Reshape the values into a 3x3 matrix<br>
matrix = values.reshape(3, 3)<br>
print(matrix)
Output:

[[1 2 3]
[4 5 6]
[7 8 9]]

48. Find the eigenvalues and eigenvectors of a matrix using NumPy.
We can use numpy.linalg.eig() function to find the eigenvalues and eigenvectors of a matrix. Here’s an example:

import numpy as np<br>
# Define your matrix<br>
matrix = np.array([[1, 2],<br>
[3, 4]])<br>
# Find eigenvalues and eigenvectors<br>
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("Eigenvalues:")<br>
print(eigenvalues)<br>
print("\nEigenvectors:")<br>
print(eigenvectors)
Output:

Eigenvalues:
[-0.37228132 5.37228132]

Eigenvectors:
[[-0.82456484 -0.41597356]
[ 0.56576746 -0.90937671]]

49. Apply broadcasting techniques to a scalar value and a 2D array.
If the arrays meet specific compatibility requirements, NumPy’s powerful broadcasting capability makes it easier to conduct actions between arrays of different forms. Combining a 2D array with a scalar value is one of the actions that may be done via broadcasting. Here’s an example:

import numpy as np<br>
# Define a scalar value<br>
scalar_value = 5<br>
# Define a 2D array<br>
array_2d = np.array([[1, 2, 3],<br>
[4, 5, 6]])<br>
# Add the scalar value to the 2D array<br>
result = array_2d + scalar_value
print("Original 2D array:")<br>
print(array_2d)<br>
print("\nScalar value:")<br>
print(scalar_value)<br>
print("\nResult after broadcasting scalar value to the 2D array:")<br>
print(result)
Output:

Original 2D array:
[[1 2 3]
[4 5 6]]

Scalar value:
5

Result after broadcasting scalar value to the 2D array:
[[ 6 7 8]
[ 9 10 11]]

50. Write a program to reshape a 1D NumPy array into a 2D array with a given number of rows.
import numpy as np<br>
original_array = np.array([2, 5, 7, 0, 1, 4])<br>
num_rows = 3<br>
reshaped_array = original_array.reshape(num_rows, -1)<br>
print("Original 1D array:")<br>
print(original_array)
print("\nReshaped 2D array:")<br>
print(reshaped_array)
Output:

Original 1D array:
[2 5 7 0 1 4]

Reshaped 2D array:
[[2 5]
[7 0]
[1 4]]