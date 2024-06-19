from filters import filters
from headers import importAll
from get_salty import generatorXnoise

import numpy
from PIL import Image
importAll()


# adds noise to original image
img = generatorXnoise.overwrite()
img0 = Image.open("salty-cameraman.jpg").convert("L")
arr = numpy.array(img0)
img0.show()


# performing filters
removed_noise_pd = filters.purposed_design(arr, 3) 
removed_noise_mf = filters.median_filter(arr, 3) 

# results
img1 = Image.fromarray(removed_noise_pd)
img1.show() # our method
img2 = Image.fromarray(removed_noise_mf)
img2.show() # median filter


"""
todo:
    add header file
    add generating noise option
    continue working on purpossed method
    find a name for so called "purpossed method"
    figure out how to perform assessment on results
"""