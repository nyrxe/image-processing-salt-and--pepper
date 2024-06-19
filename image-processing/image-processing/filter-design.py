#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#This dir is used for experimentation with filter design
#it is not a part of the project 

#impors libs
from headers import importAll
from mat_methods import bymat

importAll()
import numpy
from PIL import Image


I = Image.open("cameraman-og.png").convert("L")
I.show()

Inoisy = Image.open("salty-cameraman.jpg").convert("L")
Inoisy.show()

Inoisy_arr = numpy.array(Inoisy)
h=len(Inoisy_arr)
w=len(Inoisy_arr[0])

B = numpy.ones((h,w))
S = numpy.zeros((h,w))

#proposed filter application
#Step 2: determining the noisy pixels in the matrix

for i in range(h):
    for j in range(w):
        if(Inoisy_arr[i,j] == 0 or Inoisy_arr[i,j] == 255):
            B[i,j] = Inoisy_arr[i,j];
        
#Step 3: Set the binary mask(to detect the position)
for i in range(h):
    for j in range(w):
        if(B[i,j] != 1):
            S[i,j] = 1
        else:
            S[i,j] = 0

#step 4:        
Inoisy_before = Inoisy

k = 3        #filter size
fkh = k//2
fkw = k//2

U = numpy.pad(Inoisy_arr, (1, 1))
Y = numpy.pad(S, (1, 1))
m= 0
n= 0

i=fkh+1
j=fkw+1
c=0
e=0


for r in range(10):
    for i in range(h-fkh+1):
        for j in range(w-fkw+1):
            if(Y[i,j] != 0 and k==3):
                V = bymat.by3(U,i,j)
                Z = bymat.by3(Y,i,j)
                for c in range(3):
                    for e in range(3):
                        if(c == 2 and e ==2):
                            continue
                        else:
                            q = V[c,e]* Z[c,e] * (1/(abs(c-2) + abs(e - 2)))
                            s = Z[c,e] * (1/(abs(c-2) + abs(e - 2)))
                            m = q + m
                            n= s + n
                p = m / n
                U[i,j] = p


after_image=Image.fromarray(U)
after_image.show()                      

        
#t = 1/abs(c-2) + abs(e-2)
#q=numpy.multiply(V,Z)
#q=numpy.multiply(q,t)
                            
#s=Z[c,e] * (1/(abs(c-2) + abs(e - 2)))
#m=q + m
#n=s + n


###work-in process validation
import cv2
from math import log10, sqrt
def PSNR(original, compressed):
    mse = numpy.mean((original - compressed) ** 2)
    if(mse == 0):  # MSE is zero means no noise is present in the signal .
                  # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr

#original = cv2.imread("salty-cameraman.jpg")
#compressed = cv2.imread("ourmethod.PNG", 1)
#value = PSNR(original, compressed)
#print(f"PSNR value is {value} dB")






       
v = numpy.zeros((3, 3), dtype=float)    
        
def uceuc(b,x,y):
    v = numpy.zeros((3, 3), dtype=float)
    v[0,0] = b[x-1,y-1]
    v[0,1] = b[x,y-1]
    v[0,2] = b[x+1,y-1]

    v[1,0] = b[x-1,y]
    v[1,1] = b[x,y]
    v[1,2] = b[x+1,y]

    v[2,0] = b[x-1,y+1]
    v[2,1] = b[x,y+1]
    v[2,2] = b[x+1,y+1]

    return v

def besebes(b,x,y):
    v = numpy.zeros((5, 5), dtype=float)
    v[0,0] = b[x-1,y-1]
    v[0,1] = b[x,y-1]
    v[0,2] = b[x+1,y-1]    
    v[0,3] = b[x+2,y-1]
    v[0,4] = b[x+3,y-1] 

    v[1,0] = b[x-1,y]
    v[1,1] = b[x,y]
    v[1,2] = b[x+1,y]
    v[1,3] = b[x+2,y]
    v[1,4] = b[x+3,y]

    v[2,0] = b[x-1,y+1]
    v[2,1] = b[x,y+1]
    v[2,2] = b[x+1,y+1]
    v[2,3] = b[x+2,y+1]
    v[2,4] = b[x+3,y+1]
    
    v[3,0] = b[x-1,y+2]
    v[3,1] = b[x,y+2]
    v[3,2] = b[x+1,y+2]
    v[3,3] = b[x+2,y+2]
    v[3,4] = b[x+3,y+2]
    
    v[4,0] = b[x-1,y+3]
    v[4,1] = b[x,  y+3]
    v[4,2] = b[x+1,y+3]
    v[4,3] = b[x+2,y+3]
    v[4,4] = b[x+3,y+3]

    return v