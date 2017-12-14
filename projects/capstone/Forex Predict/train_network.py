#!/usr/bin/env python
# -*- coding: utf-8 -*-
from feed_data import data_feed
from keras.models import Sequential
from keras.layers import Dense, LSTM, Flatten, Dropout
from keras.callbacks import TensorBoard

window = 64
train_data = data_feed(filepath='data/EURUSD_M5_438K_Preprocessed.csv', window=window, percentage=0.9, dataset='train')
test_data = data_feed(filepath='data/EURUSD_M5_438K_Preprocessed.csv', window=window, percentage=0.1, dataset='test')

# design network
model = Sequential()
model.add(LSTM(64, input_shape=(window, 9)))
model.add(Dropout(0.3))

model.add(Dense(4, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')

# callbacks
tensorboard = TensorBoard(log_dir='/tmp/tensorboard', write_graph=True)

# fit network
history = model.fit_generator(
    generator=train_data.generate(),
    steps_per_epoch=1000,
    epochs=200,
    verbose=1,
    callbacks=[tensorboard],
    validation_data=test_data.generate(),
    validation_steps=100,
    shuffle=False
)