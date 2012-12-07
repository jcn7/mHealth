#run tests
import features as ff, label as la
from sklearn import linear_model
from sklearn.cross_validation import KFold
import numpy, sys
from sklearn import svm
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.preprocessing import normalize
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree

num_k_fold = 10

def compile_data(input_file, label_file):
    cf = ff.extract_features(input_file)
    truth = la.do_label(cf, label_file)
    data = []
    # we can throw away the time stamps now
    for x in cf:
        data.append(x[3])

    return data, truth

def run_lasso(data, label):
    kfold = KFold(len(label), num_k_fold)
    lasso = linear_model.LassoLarsCV()

    error = numpy.empty((num_k_fold))
    for count, (train, test) in enumerate(kfold):
        lasso.fit(data[train], label[train])
        guesses = lasso.predict(data[test])
        error[count] = sum((label[test] - guesses)**2) / num_k_fold
        print "Model: %d" % count

    final_error = error.mean(axis=0)
    print final_error

def run_naive_bayes_gaus(data, label):
    kfold = KFold(len(label), num_k_fold)
    gnb = MultinomialNB()

    accuracy = numpy.empty((num_k_fold))
    for count, (train,test) in enumerate(kfold):
        guesses = gnb.fit(data[train], label[train]).predict(data[test])      
        accuracy[count] = float(sum(guesses == label[test])) / len(guesses)

    print "naive bayes: %f" % numpy.mean(accuracy)

def run_svm(data, label):
    #data = normalize(data) - makes things worse
    lin_clf = svm.SVC(kernel='sigmoid')
    kfold = KFold(len(label), num_k_fold)
    accuracy = numpy.empty((num_k_fold))

    for count, (train, test) in enumerate(kfold):
        lin_clf.fit(data[train], label[train])
        guesses = lin_clf.predict(data[test])
        accuracy[count] = float(sum(guesses == label[test])) / len(guesses)

    print "svm: %f" % numpy.mean(accuracy)

def run_nearest_n(data, label):
    kfold = KFold(len(label), num_k_fold)
    accuracy = numpy.empty((num_k_fold))
    neigh = KNeighborsClassifier(n_neighbors=30)

    for count, (train, test) in enumerate(kfold):
        neigh.fit(data[train], label[train])
        guesses = neigh.predict(data[test])
        accuracy[count] = float(sum(guesses == label[test])) / len(guesses)

    print "nearest neighbor: %f" % numpy.mean(accuracy)

def run_d_tree(data, label):
    kfold = KFold(len(label), num_k_fold)
    accuracy = numpy.empty((num_k_fold))
    clf = tree.DecisionTreeClassifier()

    for count, (train, test) in enumerate(kfold):
        clf.fit(data[train], label[train])
        guesses = clf.predict(data[test])
        accuracy[count] = float(sum(guesses == label[test])) / len(guesses)

    print "d-tree: %f" %numpy.mean(accuracy)

def main():
    full = True
    if not full:
        x, y = compile_data('../subject_7/BHGN', '../subject_7/label.txt')
        ad = numpy.array(x)
        at = numpy.array(y)
        run_lasso(ad,at)
        run_naive_bayes_gaus(ad, at)
        run_svm(ad, at)
        run_nearest_n(ad, at)
        run_d_tree(ad,at)
    else:
        inputs = ['../subject_4/BHGN', '../subject_5/BHGN', '../subject_6/BHGN', '../subject_7/BHGN']
        labels = ['../subject_4/label.txt', '../subject_5/label.txt', '../subject_6/label.txt', '../subject_7/label.txt']

        all_data = []
        all_label = []

        for i in xrange(len(inputs)):
            d, t = compile_data(inputs[i], labels[i])
            all_data += d
            all_label += t

        d = numpy.array(all_data)
        l = numpy.array(all_label)

        run_lasso(d, l)
        run_naive_bayes_gaus(d, l)
        run_svm(d, l)
        run_nearest_n(d, l)
        run_d_tree(d,l)



main()