#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, math
import pandas as pd

class data_feed(object):
	def __init__(self, *args, **kwargs):
		# required parameters
		# filepath, window, percentage, dataset
		self.all_data = pd.read_csv(kwargs['filepath'])
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
			to_return = self.data[start:end]
		else:
			# next batch goes beyond data size
			# first, extract remaining data
			first_piece = self.data[start:]
			# now second piece
			end = self.window_size - len(first_piece)
			second_piece = self.data[:end]
			# concat both pieces
			to_return = pd.concat([first_piece, second_piece])
		# finally check if we reached the end of the dataset
		self.index_data = start + 1
		if self.index_data == self.length:
			self.index_data = 0

		to_return = to_return.as_matrix() 
		return 

	def feed(self):
		# loop through the data in order indefinitely
		while True:
			yield self.next_batch()

if __name__ == '__main__':
	feed = data_feed(filepath='data/EURUSD_M5_438K_Preprocessed.csv', window=32, percentage=0.9, dataset='train')
	#feed2 = data_feed(filepath='data/EURUSD_M5_438K_Preprocessed.csv', window=32, percentage=0.1, dataset='test')

 
