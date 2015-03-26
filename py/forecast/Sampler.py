__author__ = 'patrick'


import os.path
import csv


def load_csv(sample_file, input_count):
    if not os.path.exists(sample_file):
        print 'File "%s" not exist.' % sample_file

    inputs = []
    outputs = []

    with open(sample_file, 'rU') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            inputs.append(map(int, row[0:input_count]))
            outputs.append(row[len(row)-1])

    return inputs, outputs
