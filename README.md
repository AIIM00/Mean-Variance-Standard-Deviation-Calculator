# Mean-Variance-Standard Deviation Calculator

This project is a Python-based calculator that performs statistical analysis on a 3x3 matrix using NumPy. It calculates the mean, variance, standard deviation, maximum, minimum, and sum across rows, columns, and the entire matrix.

Built as part of the freeCodeCamp Data Analysis with Python certification projects.

Features
Accepts a list of 9 numbers and reshapes it into a 3x3 matrix

Calculates:
Mean
Variance
Standard deviation
Max and Min
Sum

Returns all results structured in a dictionary: 
The returned dictionary should follow this format:

{
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
}
If a list containing less than 9 elements is passed into the function, it should raise a ValueError exception with the message: "List must contain nine numbers." The values in the returned dictionary should be lists and not Numpy arrays.

For example, calculate([0,1,2,3,4,5,6,7,8]) should return:

{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}

Development
Write your code in mean_var_std.py. For development, you can use main.py to test your code. In order to run your code, type python3 main.py into the GitPod terminal and hit enter. This will cause the included CPython interpreter to run the main.py file.

Testing
The unit tests for this project are in test_module.py. We imported the tests from test_module.py to main.py for your convenience.

