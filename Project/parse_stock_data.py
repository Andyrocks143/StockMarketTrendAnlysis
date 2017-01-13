#! /usr/bin/env python

import csv
import pickle

stock_file = "stock/WIKI-BBY.csv"

output_file = stock_file.split('.')[0] + "_dict"

OPEN_INDEX = 1
CLOSE_INDEX = 4

stock_increase_dict = dict()

with open(stock_file, 'r') as sf:
    reader = csv.reader(sf)
    for row in reader:
        if '2016' in row[0]:
            percent_increase = (float(row[CLOSE_INDEX]) - float(row[OPEN_INDEX])) / float(row[OPEN_INDEX])
            date = row[0]
            stock_increase_dict[date] = percent_increase

with open(output_file, 'w+') as of:
    pickle.dump(stock_increase_dict, of)
