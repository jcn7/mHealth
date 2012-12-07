# apply labels to data, expects the first two column of the input data to be the unix time stamp
import csv
from datetime import datetime

LABEL_MAP = {'W' : 1, 'N1' : 2, 'N2' : 3, 'R' : 4, 'RESP' : 5}

def do_label(data, label_file):
    timestamp = []
    label =[]
    with open(input, 'r') as fin:
        label_reader = csv.reader(fin, delimiter=',')
        for row  in label_reader:
            timestamp.append(convert_time(row[0]))
            label.append(LABEL_MAP[row[1]])




def convert_time(t):
    t = t[0:t.find('.')]
    dt = datetime.strptime(t, '%m-%d-%Y %H:%M:%S')
    dt.replace(tzinfo=Eastern)
    return t.strftime * 1000