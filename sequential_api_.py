# -*- coding: utf-8 -*-
"""Sequential API .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gzJhKNdfLJmA4f8ImU3zb93cQ47bMECg
"""

from keras.layers import Lambda, concatenate
from keras import Model

import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()

model.add(Dense(512, input_shape=(784, ), activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(10, activation='softmax'))

from tensorflow.python.framework import ops

"""**Instead of adding layers one at each stage using the add method, the same model can be built by defining the layers as components of a list parameter within the Sequential class.**

# The Sequential model is a linear stack of layers.

**You can create a Sequential model by passing a list of layer instances to the constructor:**
"""

model = Sequential([
                    Dense(512, input_shape=(784, ), activation='relu'),
                    Dense(256, activation='relu'),
                    Dense(10, activation='softmax')
])

"""**Adding a name to the model**

There are **three important methods** in the **Sequentialclass** that we need to understand.


* **addmethod**: This is used to add layers to the Sequential model one by one.
*   **summarymethod:** This is used to get a summary of the model architecture. You will get a nice output that includes layer types, output shape and the number of parameters in each layer

* **popmethod**: This is used to remove layers in the model. Once called, it removes the last layer in the model. If we call it again, then it removes the next available last layer in the model, and so on.
"""

model = Sequential()
model.add(Dense(256, activation='relu'))

model.layers

!pip install tensorflow --upgrade

x = ops.ones((3, 3))
y = model(x)