# compute features for bioharness data

import sys, numpy
from math import sqrt

WINDOW_SIZE = 30

def std(data):
    return numpy.std(data)