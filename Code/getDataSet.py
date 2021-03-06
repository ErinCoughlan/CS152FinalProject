# Erin Coughlan and Vivian Wehner
# CS 152 - Neural Networks
# Data set creation

import numpy as np
from pybrain.datasets import ClassificationDataSet
from pybrain.datasets import SupervisedDataSet

def get_dataset_txt(filename):
    """
        creates a dataset for the neural network to use

        input type: string represnting filename created from numpy array
        return type: dataset
    """
    array = np.loadtxt(filename)

    # assume last field in txt is single target variable
    # and all other fields are input variables
    number_of_columns = array.shape[1]
 #   dataset = ClassificationDataSet(number_of_columns - 1, 1, nb_classes=4,
 #                               class_labels=['angry','happy','neutral','sad'])

    dataset = SupervisedDataSet(number_of_columns - 1, 4)
    
    #print array[0]
    #print array[:,:-1]
    #print array[:,-1]
    #dataset.addSample(array[:,:-1], array[:,-1])
    #dataset.addSample(array[:,:-1], array[:,-2:-1])
    dataset.setField('input', array[:,:-4])
    dataset.setField('target', array[:,-4:])

##    # one output neuron per class
##    dataset._convertToOneOfMany( )
##
##    print dataset.getField('target').transpose()
##    print dataset.getField('class').transpose()

    return dataset
