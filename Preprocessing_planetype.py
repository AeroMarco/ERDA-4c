import pygame 
import numpy as np
import codecs
import imagefuncts as imf
import math
from PIL import Image


#get input strings
    
    
def convolutor(i2u): #this is a function to detect the edges of an object in a picture. It returns a screen of a black and white image of the outline of the plane.
    f2u = 'edgedetect.txt'
    file2open =  f2u

    with codecs.open(file2open, "r", encoding = "ascii", errors = "ignore") as fltrdoc:
        fltr = fltrdoc.readlines()

    mtrx = []

    for i in range(len(fltr)):
        strow = fltr[i]
    #strow = strow[:-1]
        res = [float(j) for j in strow.split() if j.isdigit]
        mtrx.append(res)

    krnl = np.array(mtrx)
    #print(krnl)
    krnlsize = krnl.shape[0]
    pd = 0

    img = pygame.image.load(i2u)
    imgr = pygame.surfarray.pixels_red(img)
    imgg = pygame.surfarray.pixels_green(img)
    imgb = pygame.surfarray.pixels_blue(img)

    (iH, iW) = imgr.shape

    for i in range((krnlsize-1)//2):
        imgr = imf.padding(imgr)
        imgg = imf.padding(imgg)
        imgb = imf.padding(imgb)
        pd += 1

    outr = imf.convolve(imgr,krnl,pd,iH,iW)

    outg = imf.convolve(imgg,krnl,pd,iH,iW)

    outb = imf.convolve(imgb,krnl,pd,iH,iW)

    out = np.zeros((iH,iW,3),dtype=int)
    out[:,:,0] = outr
    out[:,:,1] = outg
    out[:,:,2] = outb

    imgout = pygame.pixelcopy.make_surface(out)

    
    return imgout
    
def preprocessing_type():  #this function does all the preprocessing for plane type recognition. It retuns a list of vecotors corresponding to the pictures in order form 1 to 100.
    n = 1
    n_pictures = 100 #number of pictures in dataset
    lengthlist = []
    vectorlist = []

    while n <= n_pictures: #for every picture

        
        
        matrix = pygame.PixelArray(convolutor(str(n)+'.jpg')) #get matrix of convoluted pixels in picture
        
        for j in range(len(matrix)): #for every pixel: make all non-zero values 1 and leave the rest 0
            for i in range(len(matrix[j])):
                if matrix[j][i] == 0:
                    continue
                else:
                    matrix[j][i] = 1

        print(matrix) 

        vector = []
        
        for j in range(len(matrix)): #rewrite matrix to a vector for use in the ANN
            for i in range(len(matrix[j])):
                vector.append(matrix[j][i])

        
        vectorlist.append(vector) #make a list of all vectors
        lengthlist.append(len(vector)) #make a list of the vector lenghts
        n += 1
    print(lengthlist)
    max_len = max(lengthlist) #what is the length of the longest vector?
    #print(lengthlist)
    #print(max_len)

    for a in range(len(vectorlist)): #make all vectors equal length by adding 0's to every vector until it is the length of the longest vector.
        while len(vectorlist[a]) < max_len:
            vectorlist[a].append(0)
        lengthlist[a] = len(vectorlist[a])
    #print(lengthlist)

    
    return vectorlist

def Write_up(vect):
    f= open("PreplanningPlanetype.txt","w+")
    for x in range(len(vect)):    
        str1 = ''
        for y in range(len(vect[x])):
            str1 =  str1 + str(vect[x][y]) + ' '
        f.write("\r\n" + str1)
    f.close()
    return 
Write_up(preprocessing_type())
