# TensorFlow Function

This repository contains a simple example demonstrating the use of TensorFlow's `tf.function` decorator to compile a Python function into a TensorFlow graph for optimization.

## Overview

The example defines a function to add two constant tensors using TensorFlow. It then uses the `tf.function` decorator to compile this Python function into a TensorFlow graph, enabling TensorFlow to optimize the computation for better performance.

## Code Explanation

1. **Import TensorFlow**: Importing the TensorFlow library.

2. **Constants**: Defining two constant tensors `a` and `b`.

3. **Function Definition**: Defining a function named `add` using the `@tf.function` decorator. This decorator tells TensorFlow to compile the Python function into a TensorFlow graph.

4. **Operation**: Inside the function, element-wise addition is performed using `tf.add()` to add tensors `a` and `b`.

5. **Printing**: Printing the result of the addition operation using `print(c)`.

6. **Return**: Returning the result tensor `c`.

7. **Function Call**: Calling the `add` function with the constant tensors `a` and `b` as arguments and storing the result in the `result` variable.

8. **TensorFlow Print**: Using `tf.print()` to print the result tensor value.
