# another PCA example
# http://stackoverflow.com/questions/1730600/principal-component-analysis-in-python
# takes a lot longer

import os
import cv
import numpy as np
from scipy.linalg import svd
from scipy.misc import lena
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# the underlying signal is a sinusoidally modulated image
#img = lena()
currDir = os.getcwd();
img = mpimg.imread(currDir + "/picture.png")
t = np.arange(100)
time = np.sin(0.1*t)
real = time[:,np.newaxis,np.newaxis]*np.repeat(img[np.newaxis,...],100,axis=0)

# we add some noise
noisy = real + np.random.randn(*real.shape)*255

# types*observations matrix
M = noisy.reshape(noisy.shape[0],-1).T

# singular value decomposition factorises your data matrix such that
# 
#   M = U*S*V.T     (where '*' is matrix multiplication)
# 
# U and V are the singular matrices, containing orthogonal vectors of
# unit length in their rows and columns respectively. S is a diagonal
# matrix containing the singular values of M - these values squared will
# give the proportional variance explained by each PC. since U and V
# both contain orthogonal vectors, U*V.T is a whitened version of M.
U,s,Vt = svd(M,full_matrices=False)
V = Vt.T

# sort the PCs by descending order of the singular values (i.e. by the
# proportion of total variance they explain)
ind = np.argsort(s)[::-1]
U = U[:,ind]
s = s[ind]
V = V[:,ind]

# if we use all of the PCs we can reconstruct the noisy signal perfectly
S = np.diag(s)
Mhat = np.dot(U,np.dot(S,V.T))
print "Using all PCs, MSE = %.6G" %(np.mean((M-Mhat)**2))

# if we use only the first 20 PCs the reconstruction is less accurate
Mhat2 = np.dot(U[:,:20],np.dot(S[:20,:20],V[:,:20].T))
print "Using first 20 PCs, MSE = %.6G" %(np.mean((M-Mhat2)**2))

fig,[ax1,ax2,ax3] = plt.subplots(1,3)
ax1.imshow(img)
ax1.set_title('true image')
ax2.imshow(noisy.mean(0))
ax2.set_title('mean of noisy images')
ax3.imshow(U[:,0].reshape(img.shape))
ax3.set_title('first spatial PC')

fig.savefig('out.png', dpi=100)
