#! /usr/bin/env python

import os, sys

company = sys.argv[1]

month_list = [5,6,7]

for month in month_list:
    os.system("python specific_features.py " + str(month) + ' ' + company)
