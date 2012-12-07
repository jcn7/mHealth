# compute features for bioharness data

import numpy, csv

WINDOW_SIZE = 300
N = 20

def compute_features(s_time, e_time, data):
    feature_vector = []
    feature_name = []

    # add the standard deviation
    feature_vector += [numpy.std(data)]
    feature_name += ['std']

    # add the mean
    feature_vector + [numpy.mean(data)]
    feature_name += ['mean']

    # end-to-end change
    feature_vector += [data[0] - data[-1]]
    feature_name += ['change']

    # do some fft 
    dft = numpy.real(numpy.fft.fft(data,n=N))
    feature_vector += dft.tolist()

    return (s_time, e_time, feature_name, feature_vector)
    
def extract_features(input, col=8):
    data = []
    timestamp = []
    with open(input, 'r') as fin:
        dataReader = csv.reader(fin, delimiter=',')
        for row in dataReader:
            timestamp.appen(int(row[0]))
            data.append(float(row[col]))
    i = 0
    feature_matrix[]
    while i < len(data):
        end = min(i+WINDOW_SIZE, len(data))
        r = compute_features(timestamp[i], timestamp[end], data[i:end])
        result.append(r)

    return feature_matrix



