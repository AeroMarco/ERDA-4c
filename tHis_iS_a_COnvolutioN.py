#%%
import pygame 
import numpy as np
import codecs
import imagefuncts as imf

#get input strings
i2u = '38.jpg'
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
print(krnl)
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

print("Images padded")

outr = imf.convolve(imgr,krnl,pd,iH,iW)

print("First convolution done")

outg = imf.convolve(imgg,krnl,pd,iH,iW)

print("Second convolution done")

outb = imf.convolve(imgb,krnl,pd,iH,iW)

print("Third convolution done")

out = np.zeros((iH,iW,3),dtype=int)
out[:,:,0] = outr
out[:,:,1] = outg
out[:,:,2] = outb


nimgout = pygame.pixelcopy.make_surface(out)

pygame.image.save(nimgout, "New " + i2u[:-4] + ".jpeg")

print("Image saved")












