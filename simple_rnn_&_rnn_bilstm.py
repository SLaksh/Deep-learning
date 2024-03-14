# -*- coding: utf-8 -*-
"""Simple RNN & RNN-BiLSTM.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mbcI8w3hoP2XQCIbVn_rmfHxrZx3kO0E
"""

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import numpy as np
from keras.models import Model
from keras.layers import Input, Embedding, Bidirectional, LSTM, SimpleRNN

# Sample data
sentences = ["This is a simple text", "We are learning RNN", "Keras is easy to use"]

# Initialize and fit the tokenizer
tokenizer = Tokenizer()
tokenizer.fit_on_texts(sentences)

# Transform the sentences into sequences of integers
sequences = tokenizer.texts_to_sequences(sentences)

# Pad the sequences so they all have the same length
padded_sequences = pad_sequences(sequences, maxlen=5)

padded_sequences[0]

"""## SimpleRNN

### With return sequences set to "True"
"""

# define the input shape
input_layer = Input(shape=(5,))

emd_inp = Embedding(30, 1, input_length = 5)(input_layer)

# create SimpleRNN layer
simple_rnn = SimpleRNN(10, activation='tanh', return_sequences=True)(emd_inp)

# create model
model = Model(inputs=input_layer, outputs=simple_rnn)

model.predict(padded_sequences)

"""### With return sequences set to "False"
"""

# define the input shape
input_layer = Input(shape=(5,))

emd_inp = Embedding(30, 1, input_length = 5)(input_layer)

# create SimpleRNN layer
simple_rnn = SimpleRNN(10, activation='tanh', return_sequences=False)(emd_inp)

# create model
model = Model(inputs=input_layer, outputs=simple_rnn)

# Now you can use this data as input to your model
output = model.predict(padded_sequences)
output

"""## Bi-LSTM"""

# define the input shape
input_layer = Input(shape=(5,))

emd_inp = Embedding(30, 1, input_length = 5)(input_layer)

# create SimpleRNN layer
simple_rnn = Bidirectional(LSTM(10, activation='tanh', return_sequences=False), merge_mode="concat")(emd_inp)

# create model
model = Model(inputs=input_layer, outputs=simple_rnn)

# Now you can use this data as input to your model
output = model.predict(padded_sequences)
output

