# Erin Coughlan and Vivian Wehnes

import numpy as np
from pybrain.datasets import ClassificationDataSet

def get_dataset_txt(filename):

    array = np.loadtxt(filename)

    # assume last field in txt is single target variable
    # and all other fields are input variables
    number_of_columns = array.shape[1]
    dataset = ClassificationDataSet(number_of_columns - 1, 1, nb_classes=4,
                                class_labels=['angry','happy','neutral','sad'])

    print array[0]
    #print array[:,:-1]
    #print array[:,-1]
    #dataset.addSample(array[:,:-1], array[:,-1])
    #dataset.addSample(array[:,:-1], array[:,-2:-1])
    dataset.setField('input', array[:,:-1])
    dataset.setField('target', array[:,-1:])

    # one output neuron per class
    dataset._convertToOneOfMany( )

    return dataset

def get_dataset_csv(filename):

    array = np.loadtxt(filename, delimiter=',')

    # assume last field in txt is single target variable
    # and all other fields are input variables
    number_of_columns = array.shape[1]
    dataset = ClassificationDataSet(number_of_columns - 1, 1, nb_classes=4,
                                class_labels=['angry','happy','neutral','sad'])

    print array[0]
    #print array[:,:-1]
    #print array[:,-1]
    #dataset.addSample(array[:,:-1], array[:,-1])
    #dataset.addSample(array[:,:-1], array[:,-2:-1])
    dataset.setField('input', array[:,:-1])
    dataset.setField('target', array[:,-1:])

    return dataset
