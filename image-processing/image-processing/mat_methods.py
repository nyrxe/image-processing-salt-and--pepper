#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy 

class bymat:
    def __init__(self,by3,by5):
        self.by3 =by3
        self.by5 =by5

    def by3(b,x,y):
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


    def by5(b,x,y):
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
