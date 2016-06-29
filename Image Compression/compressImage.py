from loadImage import loadFromFile, return2dImageMatrix
import numpy as np
import random as rd

def randomInitialize(X, K):
	"""randomly initialize few datapoints as points for 
	centroids for applying the kmeans algorithm"""
	a,b = X.shape
	randIndexes = np.random.randint(a, size=K)
	return X[randIndexes,:]

def findClosestCentroid(X, centroids):
	"""find the closest centroids and and return the 
	centroid index number in an array"""
	K,n = centroids.shape
	# Now n has the no of features and K has the no of clusters.
	closestCentroidNo = np.zeros(len(X))
	noOfDataPoints = len(X)
	for i in range(noOfDataPoints):
		dataPoint = X[i];
		queryMat = np.tile(dataPoint, (K,1))
		squared_distance = np.square(centroids - queryMat).sum(1)
		min_squared_distance = min(squared_distance)
		indexOfMinElement = np.where(squared_distance == min_squared_distance)[0][0]
		closestCentroidNo[i] = indexOfMinElement
		# this gets kind of depenent issue
	return closestCentroidNo



def computeCentroids(X, closestCentroidNo, K):
	"""Function computing the centroid locations again 
	to shift the position of the new centroid"""
	m,n = X.shape
	centroids = np.zeros((K,n))
	for i in range(K):
		indices = (closestCentroidNo == i)
		for j in range(n):
			if(indices.mean()!=0):
				centroids[i,j] = sum(X[:,j]*indices)/((indices.mean())*len(indices))
	return centroids
	


ImgName = '12.jpg'
Imgarray = loadFromFile(ImgName)
a,b,c = Imgarray.shape
TwoDarray = return2dImageMatrix(Imgarray).transpose()
# I know this is shit code.
K = int(raw_input("Enter the no of clusters: "))
A = randomInitialize(TwoDarray,K)
max_iter = 10
for iter in range(max_iter):
	print "Started with iteration " + str(iter)
	closestCentroidNo = findClosestCentroid(TwoDarray,A)
	centroids = computeCentroids(TwoDarray, closestCentroidNo, K)
	print "Done with iteration " + str(iter) 
for iter in range(len(TwoDarray)):
	TwoDarray[iter] = centroids[closestCentroidNo[iter]]
print "The centroids are"
for centroid in centroids:
	print centroid
TwoDarray = np.fliplr(TwoDarray)
ThreeD = TwoDarray.reshape(a,b,c)
import Image
Im = Image.fromarray(ThreeD)
Im.save("Kclusters-{}".format(ImgName))




