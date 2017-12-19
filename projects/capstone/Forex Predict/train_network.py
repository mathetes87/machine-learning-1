#!/usr/bin/env python
# -*- coding: utf-8 -*-
from feed_data import data_feed
from keras.models import Sequential
from keras.layers import Dense, LSTM, Flatten, Dropout
from keras.callbacks import TensorBoard, ModelCheckpoint

window = 64
train_data = data_feed(filepath='data/EURUSD_M5_438K_Preprocessed.csv', window=window, percentage=0.9, dataset='train')
test_data = data_feed(filepath='data/EURUSD_M5_438K_Preprocessed.csv', window=window, percentage=0.1, dataset='test')

# design network
model = Sequential()
model.add(LSTM(64, input_shape=(window, 9)))
model.add(Dropout(0.3))

model.add(Dense(4, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam',
              metrics=['acc'])

# callbacks
tensorboard = TensorBoard(log_dir='/data/tensorboard', write_graph=True)
checkpoint = ModelCheckpoint('LSTM_64_03_best.h5', monitor='val_loss', save_best_only=True)

# fit network
history = model.fit_generator(
    generator=train_data.generate(),
    steps_per_epoch=5000,
    epochs=400,
    verbose=1,
    callbacks=[tensorboard, checkpoint],
    validation_data=test_data.generate(),
    validation_steps=2500,
    shuffle=False
)

# output history to plot or whatnot
print history
