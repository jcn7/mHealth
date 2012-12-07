#run tests
import features as ff, label as la
from sklearn import linear_model
from sklearn.cross_validation import KFold
import numpy, sys

num_k_fold = 10

def compile_data(input_file, label_file):
    cf = ff.extract_features(input_file)
    truth = la.do_label(cf, label_file)
    data = []

    # we can throw away the time stamps now
    for x in cf:
        data.append(x[3])
    print len(truth)

compile_data(sys.argv[1], sys.argv[2])