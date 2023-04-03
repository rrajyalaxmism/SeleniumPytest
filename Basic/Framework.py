import time
from selenium import webdriver
import csv

def read_csv_file(csv_filename, key):
    file = open(csv_filename)
    dictreader = csv.DictReader(file)
    for val in dictreader:
        if val['KEY'] == key:
            return val['VALUE']
