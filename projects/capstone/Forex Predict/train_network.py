#!/usr/bin/env python
# -*- coding: utf-8 -*-
from feed_data import data_feed
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM

train_data = data_feed(filepath='data/EURUSD_M5_438K_Preprocessed.csv', window=32, percentage=0.9, dataset='train')