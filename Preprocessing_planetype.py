#edgedetection
#get vector with all plane pixels
#Direction facing change by making the length with the largest amount of pixels the plane length
#then making the edge with the extra width the tail
#feed vector (normalized to a biger size to  work with large images) into an ANN
#preprocessing done

import pygame 
import numpy as np
import codecs
import imagefuncts as imf

#get input strings
    
    
def convolutor(i2u):
    f2u = 'edgedetect.txt'
    file2open =  f2u

    with codecs.open(file2open, "r", encoding = "ascii", errors = "ignore") as fltrdoc:
        fltr = fltrdoc.readlines()

    strows = []
    mtrx = []

#use lIst COmprEhenSioN to get the matrix of the values
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

vector = pygame.PixelArray(convolutor('1.jpg'))

for j in range(len(vector)):
    for i in range(len(vector[j])):
        if vector[j][i] == 0:
            continue
        else:
            vector[j][i] = 1
print(vector)


