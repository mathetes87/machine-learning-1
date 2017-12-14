#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys, math
import pandas as pd
import numpy as np

class data_feed(object):
	def __init__(self, *args, **kwargs):
		# required parameters
		# filepath, window, percentage, dataset
		self.filepath = os.path.join(sys.path[0], kwargs['filepath'])
		self.all_data = pd.read_csv(self.filepath).drop(['time'], axis=1)
		if kwargs['dataset'] == 'train':
			self.data = self.all_data[:int(len(self.all_data)*kwargs['percentage'])]
		if kwargs['dataset'] == 'test':
			self.data = self.all_data[-int(len(self.all_data)*kwargs['percentage']):]
		self.length = len(self.data)
		self.window_size = kwargs['window']
		self.index_data = 0

	def next_batch(self):
		start = self.index_data
		# check that next batch doesn't go beyond data size
		if self.index_data + self.window_size < self.length:
			end = start + self.window_size
			to_return = self.data[start:end+1]
		else:
			# next batch goes beyond data size
			# first, extract remaining data
			first_piece = self.data[start:]
			# now second piece
			end = self.window_size - len(first_piece)
			second_piece = self.data[:end+1]
			# concat both pieces
			to_return = pd.concat([first_piece, second_piece])
		# finally check if we reached the end of the dataset
		self.index_data = start + 1
		if self.index_data == self.length:
			self.index_data = 0

		to_return = to_return.as_matrix()

		X = to_return[:-1]
		# if close price is less than 0.03% of previous close price, we will label it as a shy movement
		# labels: way_up, shy_up, shy_down, way_down as a onehot vector
		# this threshold was selected by trial and error. It gives, for the first 50,000 candles, 
		# a distribution of [6402, 18188, 19202, 6208] which seems about right
		last_candle = X[-1][1]
		next_candle = to_return[-1][1]
		relation = float(next_candle - last_candle)/last_candle
		percentage = 0.03/100
		if relation > percentage:
			move = 3
		elif relation >= 0:
			move = 2
		elif relation > -percentage:
			move = 1
		else:
			move = 0
		y = np.zeros(4)
		y[move] = 1

		X = np.asarray(X, dtype=np.float32)
		X = np.expand_dims(X, axis=0)
		y = np.asarray(y, dtype=np.float32)
		y = np.expand_dims(y, axis=0)

		return (X, y)

	def generate(self):
		# loop through the data in order indefinitely
		while True:
			yield self.next_batch()

if __name__ == '__main__':
	feed = data_feed(filepath='data/EURUSD_M5_438K_Preprocessed.csv', window=2, percentage=0.9, dataset='train')
	print feed.next_batch()
	#feed2 = data_feed(filepath='data/EURUSD_M5_438K_Preprocessed.csv', window=32, percentage=0.1, dataset='test')

 
