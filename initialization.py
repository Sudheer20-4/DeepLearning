# -*- coding: utf-8 -*-
"""Initialization

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lEC__oooBY1rqlB1lHiYPONa_zpe34d9

# Zero Initialization

**import necessary libraries**
"""

import tensorflow as tf
from tensorflow.keras import layers

"""**Define the initializer and the dense layer**"""

initializer = tf.keras.initializers.Zeros()
layer = tf.keras.layers.Dense(3, kernel_initializer=initializer)

"""**Build the layer (usually this is not required explicitly in modern versions of TensorFlow)**"""

layer.build(input_shape=(None, 5))  # The input shape needs to be provided if not used in a model

"""**Print the weights of the layer**"""

print(layer.get_weights())

"""# Random Normal Distribution

**import necessary libraries**
"""

import tensorflow as tf
from tensorflow.keras import layers

""" **Define the initializer with mean 0 and standard deviation 1**

"""

initializer = tf.keras.initializers.RandomNormal(mean=0.0, stddev=1.0)

"""**Create the Dense layer with 3 units and the RandomNormal initializer**"""

layer = tf.keras.layers.Dense(3, kernel_initializer=initializer)

"""**Provide input shape to build the layer**"""

layer.build(input_shape=(None, 5))  # Example: batch size is None, and input dimension is 5

"""**Print the weights of the layer**"""

print(layer.get_weights())

"""# Random Uniform Initialization

**import necessary libraries**
"""

import tensorflow as tf
from tensorflow.keras import layers

"""**Define the initializer with RandomUniform with minval=0 and maxval=1**"""

initializer = tf.keras.initializers.RandomUniform(minval=0.0, maxval=1.0)

"""**Create the Dense layer with 3 units and the RandomUniform initializer**"""

layer = tf.keras.layers.Dense(3, kernel_initializer=initializer)

"""**Provide the input shape to build the layer**"""

layer.build(input_shape=(None, 5))  # Example: batch size is None, and input dimension is 5

"""**Print the weights of the layer**"""

print(layer.get_weights())