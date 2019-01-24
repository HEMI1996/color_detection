from scipy.spatial import distance as dist
from collections import OrderedDict
import numpy as np
import cv2
 
class ColorLabeler:
	def __init__(self):
		# initializing the colors dictionary
		colors = OrderedDict({
			"red": (255, 0, 0),
			"green": (0, 255, 0),
			"blue": (0, 0, 255)})
 
		# allocating memory for lab image
		self.lab = np.zeros((len(colors), 1, 3), dtype="uint8")
		self.colorNames = []
 
		for (i, (name, rgb)) in enumerate(colors.items()):
			# update the L(lightness)*a(red, green)*b(blue, yellow)* array and the color names list
			self.lab[i] = rgb
			self.colorNames.append(name)
 
		self.lab = cv2.cvtColor(self.lab, cv2.COLOR_RGB2LAB)

	def label(self, image, c):
		# constructing a mask for the contour and then computing the average lab value for the masked region
		mask = np.zeros(image.shape[:2], dtype="uint8")
		cv2.drawContours(mask, [c], -1, 255, -1)
		mask = cv2.erode(mask, None, iterations=2)
		mean = cv2.mean(image, mask=mask)[:3]
 
		# minimum distance found upto now
		minDist = (np.inf, None)
 
		# looping over the known lab color values
		for (i, row) in enumerate(self.lab):
			# compute the distance between the current lab color value and the mean of the image
			d = dist.euclidean(row[0], mean)
 
			# if the distance is smaller than the current distance, then update the bookkeeping variable
			if d < minDist[0]:
				minDist = (d, i)
 
		# return the name of the color with the smallest distance
		return self.colorNames[minDist[1]]