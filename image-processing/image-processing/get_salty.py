import random
import cv2
from PIL import Image

class generatorXnoise:
    def __init__(self, generate, overwrite):
        self.generate = generate
        self.overwrite = overwrite
        
    def generate(img):
        # Getting the dimensions of the image
    	row , col = img.shape
    	
        #randomly putting 170000 salt
    	number_of_pixels = 190000
    	for i in range(number_of_pixels):
    	
    		# Pick a random y coordinate
    		y_coord=random.randint(0, row - 1)
    		
    		# Pick a random x coordinate
    		x_coord=random.randint(0, col - 1)
    		
    		# Color that pixel to white
    		img[y_coord][x_coord] = 255
    		

        #randomly putting 170000 salt
    	number_of_pixels = 190000
    	for i in range(number_of_pixels):
    	
    		# Pick a random y coordinate
    		y_coord=random.randint(0, row - 1)
    		
    		# Pick a random x coordinate
    		x_coord=random.randint(0, col - 1)
    		
    		# Color that pixel to black
    		img[y_coord][x_coord] = 0
    		
    	return img
    
    def overwrite():

        # salt-and-pepper noise can
        # be applied only to grayscale images
        # Reading the color image in grayscale image
        img = cv2.imread('cameraman-og.png',
        				cv2.IMREAD_GRAYSCALE)

        #Storing the image
        cv2.imwrite('salty-cameraman.jpg', 
                    generatorXnoise.generate(img))

        return img