# Erin Coughlan and Vivian Wehner
# Neural Network with Contour Plot

from pybrain.datasets import ClassificationDataSet
from pybrain.utilities import percentError
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure.modules import SoftmaxLayer

from pylab import ion, ioff, figure, draw, contourf, clf, show, hold, plot
from scipy import diag, arange, meshgrid, where
from numpy.random import multivariate_normal


# set up the dataset (not sure what these values mean)
means = [(-1,0), (2,4), (3,1), (1,2)]
cov = [diag([1,1]), diag([0.5,1.2]), diag([1.5,0.7]), diag([2,.9])]
alldata = ClassificationDataSet(2, 1, nb_classes=4,
                                class_labels=['angry','happy','neutral','sad'])

for n in xrange(400):
    for klass in range(4):
        input = multivariate_normal(means[klass],cov[klass])
        alldata.addSample(input, [klass])

# randomly split data into training and testing
tstdata, trndata = alldata.splitWithProportion(0.25)

# one output neuron per class -- we already did this in 
trndata._convertToOneOfMany( )
tstdata._convertToOneOfMany( )

# info about dataset
print "Number of training patterns: ", len(trndata)
print "Input and output dimensions: ", trndata.indim, trndata.outdim
print "First sample (input, target, class):"
print trndata['input'][0], trndata['target'][0], trndata['class'][0]

# make a feed-forward network with 5 hidden units
fnn = buildNetwork(trndata.indim, 5, trndata.outdim, outclass=SoftmaxLayer)

# make the back propogation trainer
trainer = BackpropTrainer(fnn, dataset=trndata)

# square grid of data points to get contour plot for visualization
ticks = arange(-3.,6.,0.2)
X, Y = meshgrid(ticks, ticks)
# need column vectors in dataset, not arrays
griddata = ClassificationDataSet(2,1, nb_classes=4)
for i in xrange(X.size):
    griddata.addSample([X.ravel()[i],Y.ravel()[i]], [0])
griddata._convertToOneOfMany()  # this is still needed to make the fnn feel comfy

# training time
for i in range(20):
    trainer.trainEpochs(1) # usually a larger number, but 1 for visualization

    # evaluate the network
    trnresult = percentError( trainer.testOnClassData(),
                              trndata['class'] )
    tstresult = percentError( trainer.testOnClassData(
           dataset=tstdata ), tstdata['class'] )

    print "epoch: %4d" % trainer.totalepochs, \
          "  train error: %5.2f%%" % trnresult, \
          "  test error: %5.2f%%" % tstresult

    # change it back into a quare array
    out = fnn.activateOnDataset(griddata)
    out = out.argmax(axis=1)  # the highest output activation gives the class
    out = out.reshape(X.shape)

    # plot the test data and grid as a contour plot
    figure(1)
    ioff()  # interactive graphics off
    clf()   # clear the plot
    hold(True) # overplot on
    for c in [0,1,2,3]:
        here, _ = where(tstdata['class']==c)
        plot(tstdata['input'][here,0],tstdata['input'][here,1],'o')
    if out.max()!=out.min():  # safety check against flat field
        contourf(X, Y, out)   # plot the contour
    ion()   # interactive graphics on
    draw()  # update the plot

# keep the plot up
ioff()
show()

