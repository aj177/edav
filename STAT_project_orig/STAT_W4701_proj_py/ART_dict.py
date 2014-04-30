__author__ = 'Aarti'

import csv
import pandas as pd


txt = open("ART_dict.csv","rU")

file_data = txt.readlines()
dictionary = {}
#file_data.readlines()   # skip the first line
for key in file_data:
    key = key.replace('"', '').strip()
    k = key.split(",")
    dictionary[k[0]] = k[1]


print dictionary


