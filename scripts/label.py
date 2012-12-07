# apply labels to data, expects the first two column of the input data to be the unix time stamp
import csv, pytz
from datetime import datetime

LABEL_MAP = {'W' : 1, 'N1' : 2, 'N2' : 3, 'N3' : 4, 'R' : 5, 'RESP' : 6}
eastern = pytz.timezone("US/Eastern")

def do_label(data, label_file):
    timestamp = []
    label =[]
    init = 1

    results = []
    with open(label_file, 'r') as fin:
        label_reader = csv.reader(fin, delimiter=',')
        for row  in label_reader:
            timestamp.append(convert_time(row[0]))
            if len(row) < 2:
                label.append(1)
            else:
                label.append(LABEL_MAP[row[1]])

    for e in data:
        start = e[0]
        end = e[1]

        s_i = max(find_first(start, init, timestamp)-1, 0)
        e_i = find_first(end, s_i, timestamp)
        init = e_i

        l = [0]*(len(LABEL_MAP)+1)
        for s in label[s_i:e_i]:
            l[s] += 1

        results.append(compute_label(l))
    return results

def convert_time(t):
    t = t[0:t.find('.')]
    dt = datetime.strptime(t, '%m-%d-%Y %H:%M:%S')
    dt2 = eastern.localize(dt)
    return int(dt2.strftime('%s')) * 1000

def find_first(t, start, list):
    i = start
    while i < len(list):
        if list[i] > t:
            return i
        i += 1
    return len(list)

def compute_label(list):
    if len(list) == 0 or max(list) == 0:
        return 1
    return list.index(max(list))