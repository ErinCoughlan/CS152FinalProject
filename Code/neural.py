# It's time for the neural network
# Using PyBrain
# Erin Coughlan and Vivian Wehner

import pybrain
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

# Building a neural network that has 2 inputs, 3 hiddne layers, and 1 output
# Already is initialized with random values
net = buildNetwork(2,3,1, bias = True)

# constructing the data set (for XOR -- two inputs, one output)
ds = SupervisedDataSet(2, 1)
ds.addSample((0,0), (0,))
ds.addSample((0,1), (1,))
ds.addSample((1,0), (1,))
ds.addSample((1,1), (0,))

# using back propgation to train
trainer = BackpropTrainer(net, ds)
trainer.train() # only one epoch, returns double proportaional to error
trainer.trainUntilConvergence() # returns an tuple? of errors for each epoch

# get the weights
weights = net.params

print weights
