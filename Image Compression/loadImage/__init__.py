import cv2
import numpy as np
def loadFromFile(path):
	"""Function to load image from file and return the numpy array"""
	im = cv2.imread(path)
	return im

def return2dImageMatrix(Threedarray):
	"""A 3d Image Matrix in numpy is of the form n*m*3, However, the 
	first n denotes the no of 2d matrices. Thus first need to convert
	the image matrix to 3*n*m and then reshape it so that the dimension 
	becomes (3,n*m)"""
	im = Threedarray.transpose(2,0,1).reshape(3,-1)
	return im



	
