import numpy as np
def padding(img):
    height = img.shape[0]+2
    width = img.shape[1]+2
    pimg = np.zeros((height,width))
    #padding in the corners
    pimg[0,0] = img[0,0]
    pimg[height-1,0]= img[img.shape[0]-1,0]
    pimg[height-1,width-1] = img[img.shape[0]-1,img.shape[1]-1]
    pimg[0,width-1] = img[0,img.shape[1]-1]
    #padding the sides
    pimg[0:height-2,0] = img[:,0]
    pimg[0:height-2,width-1] = img[:,img.shape[1]-1]
    pimg[0,0:width-2] = img[0,:]
    pimg[height-1,0:width-2] = img[img.shape[0]-1,:]
    #filling in the middle
    pimg[0:height-2,0:width-2] = img[:,:]
    return pimg
        
def convolve(img,krnl,pad,iH,iW):
    out = np.zeros((iH, iW))
    for y in np.arange(pad, iH + pad):
        for x in np.arange(pad, iW + pad):
            regofI = img[y-pad:y+pad+1,x-pad:x+pad+1]
            conv = np.multiply(regofI,krnl)
            conv = round(np.sum(conv))
            if conv > 255:
                conv = 255
            if conv < 0:
                conv = 0
            out[y-pad,x-pad] = conv
    return out




