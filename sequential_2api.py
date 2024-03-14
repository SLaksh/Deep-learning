# -*- coding: utf-8 -*-
"""Sequential_2API.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UR4_ZnUEor8w7LNStJscSsq-0DKbfP29
"""

from keras.models import Sequential
from keras.layers import Dense, Activation

model = Sequential([
    Dense(32, input_dim=784),
    Activation('relu'),
    Dense(10),
    Activation('softmax'),
])

"""

*   **Keras Dense layer** is the layer that contains all the neurons that are deeply connected within themselves.

*   This means that every neuron in the dense layer takes the input from all the other neurons of the previous layer. We can add as many dense layers as required.

"""

model = Sequential()
model.add(Dense(32, input_dim=784))   # it means 784 input parameters, with 32 neurons in the first hidden layer
model.add(Activation('relu'))

model = Sequential()
model.add(Dense(32, input_shape=(784,)))

model = Sequential()
model.add(Dense(32, batch_input_shape=(None, 784)))

model = Sequential()
model.add(Dense(32, input_dim=784))

from tensorflow.keras.layers import LSTM

"""**Long short-term memory (LSTM)** network is a recurrent neural network (RNN), aimed to deal with the vanishing gradient problem present in traditional RNNs

# **What is Vanishing Gradient problem ?**


1.  The vanishing gradients problem is one example of unstable behavior that you may encounter when training a deep neural network.

2.   It describes the situation where a deep multilayer feed-forward network or a recurrent neural network is unable to propagate useful gradient information from the output end of the model back to the layers near the input end of the model.

3. The result is the general inability of models with many layers to learn on a given dataset, or for models with many layers to prematurely converge to a poor solution.
"""

model = Sequential()
model.add(LSTM(32, input_shape=(10, 64)))

"""# **Merge the Layer**

Multiple Sequential instances can be merged into a single output via a **Concatenate layer**. The output is a layer that can be added as first layer in a new Sequential model. For instance, here's a model with two separate input branches getting merged:
"""

from keras.layers import Concatenate
left_branch = Sequential()
left_branch.add(Dense(32, input_dim=784))

right_branch = Sequential()
right_branch.add(Dense(32, input_dim=784))

merged = Concatenate([left_branch, right_branch])

final_model = Sequential()
final_model.add(merged)
final_model.add(Dense(10, activation='softmax'))

"""![merge.png](data:image/png;base64,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2zY1hHGsTWNVBOv+UrX2z85F6tdHsDgfy0DS5RLBDfW3Wwt6ehlJVztZLgmAAAUlrwNfE4AwxIgGDpac6RQ+Xjsi1g49XvMpSLxEcMNGD3QkkA0EuDwkG3qJdUwJgWwQkikBEWch5BYnMEbPOgIUlFnXZawwCZAACZBAKglQUKaSNssiARIgARLIOgIUlFnXZawwCZAACZBAKglQUKaSNssiARIgARLIOgIUlFnXZawwCZAACZBAKglQUKaSNssiARIgARLIOgIUlFnXZawwCZAACZBAKglQUKaSNssiARIgARLIOgIUlFnXZawwCZAACZBAKglQUKaSNssiARIgARLIOgIUlFnXZawwCZAACZBAKgnww82ppO2zsvD5qmR8ZNhnGNncKATwGbSdO3dKkSJFosRiEAkUjAC/HlIwfkwdhQC+DjFr1iz5888/o8RikEPg+++/lxtvvFHGjBkjBx10kOPN3ygEKlSoQCEZhQ+DEkOAI8rEcGQuJFBgAkuWLJGmTZsKPmhcrVq1AufHDEiABBJDgHOUieHIXEiABEiABHKUAAVljnYsm0UCJEACJJAYAhSUieHIXEiABEiABHKUAAVljnYsm0UCJEACJJAYAhSUieHIXEiABEiABHKUAAVljnYsm0UCJEACJJAYAhSUieHIXEiABEiABHKUAAVljnYsm0UCJEACJJAYAhSUieHIXEiABEiABHKUAAVljnYsm0UCJEACJJAYAhSUieHIXEiABEiABHKUAAVljnYsm0UCJEACJJAYAhSUieHIXEiABEiABHKUAAVljnYsm0UCJEACJJAYAhSUieHIXEiABEiABHKUAAVljnYsm0UCJEACJJAYAhSUieHIXEiABEiABHKUAAVljnYsm0UCJEACJJAYAhSUieHIXEiABEiABHKUAAVljnYsm0UCJEACJJAYAhSUieHIXEiABEiABHKUAAVljnYsm0UCJEACJJAYAhSUieHIXEiABEiABHKUAAVljnYsm0UCJEACJJAYAhSUieHIXEiABEiABHKUAAVljnYsm0UCJEACJJAYAhSUieHIXEiABEiABHKUAAVljnYsm0UCJEACJJAYAhSUieHIXEiABEiABHKUAAVljnYsm0UCJEACJJAYAhSUieHIXEiABEiABHKUAAVljnYsm0UCJEACJJAYAkUTkw1zIQESiJfAnj17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)

# **Compilation**

Before training a model, you need to configure the learning process, which is done via the compile method.
It receives three arguments:

*   **an optimizer**. This could be the string identifier of an existing optimizer (such as rmsprop or adagrad), or an instance of the Optimizer class. See: optimizers.

*   **a loss function.** This is the objective that the model will try to minimize. It can be the string identifier of an existing loss function (such as categorical_crossentropy or mse), or it can be an objective function. See: objectives.
*  **a list of metrics.** For any classification problem you will want to set this to metrics=['accuracy']. A metric could be the string identifier of an existing metric or a custom metric function. Custom metric function should return either a single tensor value or a dict metric_name -> metric_value.
"""

model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# for a binary classification problem
model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# for a mean squared error regression problem
model.compile(optimizer='rmsprop',
              loss='mse')

# for custom metrics
import keras.backend as K

def mean_pred(y_true, y_pred):
    return K.mean(y_pred)

def false_rates(y_true, y_pred):
    false_neg = ...
    false_pos = ...
    return {
        'false_neg': false_neg,
        'false_pos': false_pos,
    }

model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy', mean_pred, false_rates])

"""# **Training**


1.   Keras models are trained on Numpy arrays of input data and labels.
2.   For training a model, you will typically use the fit function.
3.   for a single-input model with 2 classes (binary)


"""

model = Sequential()
model.add(Dense(1, input_dim=784, activation='sigmoid'))
model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# generate dummy data
import numpy as np
data = np.random.random((1000, 784))
labels = np.random.randint(2, size=(1000, 1))

# train the model, iterating on the data in batches
# of 32 samples
model.fit(data, labels, epochs=10, batch_size=32)

!pip install np_utils

left_branch = Sequential()
left_branch.add(Dense(32, input_dim=784))

right_branch = Sequential()
right_branch.add(Dense(32, input_dim=784))

merged = Concatenate([left_branch, right_branch])

model = Sequential()
model.add(merged)
model.add(Dense(10, activation='softmax'))

model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# generate dummy data
import numpy as np
from tensorflow.keras.utils import to_categorical
data_1 = np.random.random((1000, 784))
data_2 = np.random.random((1000, 784))

# these are integers between 0 and 9
labels = np.random.randint(10, size=(1000, 1))
# we convert the labels to a binary matrix of size (1000, 10)
# for use with categorical_crossentropy
labels = to_categorical(labels, 10)

# train the model
# note that we are passing a list of Numpy arrays as training data
# since the model has 2 inputs
model.fit([data_1, data_2], labels, epochs=10, batch_size=32)

model.summary()