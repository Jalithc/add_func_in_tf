'''import the libraries'''
import tensorflow as tf

a = tf.constant([2], name = 'constant_a')
b = tf.constant([3], name = 'constant_b')

#create a function
@tf.function
def add(a,b):
    c = tf.add(a, b)
    #c = a + b is also a way to define the sum of the terms
    print(c)
    return c

result = add(a,b)
tf.print(result[0])
