import numpy
from PIL import Image

from mat_methods import bymat

class filters:
    def __init__(self, median, purposed_design):
        self.median = median
        self.purposed_design = purposed_design
        
    def median_filter(data, filter_size):
        temp = []
        indexer = filter_size // 2
        data_final = []
        data_final = numpy.zeros((len(data),len(data[0])))
        for i in range(len(data)):

            for j in range(len(data[0])):

                for z in range(filter_size):
                    if i + z - indexer < 0 or i + z - indexer > len(data) - 1:
                        for c in range(filter_size):
                            temp.append(0)
                    else:
                        if j + z - indexer < 0 or j + indexer > len(data[0]) - 1:
                            temp.append(0)
                        else:
                            for k in range(filter_size):
                                temp.append(data[i + z - indexer][j + k - indexer])

                temp.sort()
                data_final[i][j] = temp[len(temp) // 2]
                temp = []
        return data_final
    
    
    def purposed_design(data, k=3):

        h=len(data)
        w=len(data[0])

        B = numpy.ones((h,w))
        S = numpy.zeros((h,w))

        #proposed filter application
        #Step 2: determining the noisy pixels in the matrix

        for i in range(h):
            for j in range(w):
                if(data[i,j] == 0 or data[i,j] == 255):
                    B[i,j] = data[i,j];
                
        #Step 3: Set the binary mask(to detect the position)
        for i in range(h):
            for j in range(w):
                if(B[i,j] != 1):
                    S[i,j] = 1
                else:
                    S[i,j] = 0

        #step 4:        

        fkh = k//2
        fkw = k//2

        U = numpy.pad(data, (1, 1))
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
        return U     


"""
1. allocate outputPixelValue[image width][image height]
2. allocate window[window width × window height]
3. edgex := (window width / 2) rounded down
4. edgey := (window height / 2) rounded down
    

    for x from edgex to image width - edgex do
    for y from edgey to image height - edgey do
        i = 0
        for fx from 0 to window width do
            for fy from 0 to window height do
                window[i] :=
                inputPixelValue[x + fx - edgex][y + fy - edgey]
                i := i + 1
        sort entries in window[]
        outputPixelValue[x][y] :=
        window[window width * window height / 2]    
"""























                     