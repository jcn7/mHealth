# compute features for bioharness data

import sys, numpy, scipy
from math import sqrt

WINDOW_SIZE = 30

def compute_features(data):
    feature_vector = []
    feautre_name = []

    # add the standard deviation
    feature_vector.append(numpy.std(data))
    feature_name.append('std')

    # add the mean
    feature_vector.append(scipy.mean(data))
    feature_vector.append('mean')

    

