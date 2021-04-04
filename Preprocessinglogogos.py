#Get pixels of image
#make appropriate number of bins
#turn pixel color percentages into vector
#feed vector into ANN

from PIL import Image
import numpy as np
import codecs
import imagefuncts as imf
import math
import matplotlib




def preprocessing_logos():  #this function does all the preprocessing for plane logo recognition. It retuns a list of vectors corresponding to the pictures in order form 1 to 100.
    #this program will find the top 2000 colors in rgb format

    n = 1
    n_pictures = 100 #number of pictures in dataset
    lengthlist = []
    vectorlist = []
    while n <= n_pictures: #for every picture

        lengthlist = []
        img = Image.open(str(n)+'.jpg')
        
        im_rgb = img.convert('RGB')
        colors = im_rgb.getcolors(maxcolors=200000)
          
        if (n not in  [35,61]): # These 2 images show up as not having any colors, as in the value of the color just comes up as none, but they seem to still wotrk with other processes so ive kept them in just in case
            tots = list(img.getdata())
            pixmax = len(tots)
            a = []
            b = []
            c = []
            used = []
            for x in range (13):
                a.append(math.floor((x*255)/13))
                b.append(math.floor((x*255)/13))
                c.append(math.floor((x*255)/13))
            for x in (a):
                for y in (b):
                    for z in (c):
                        falsetot = 0
                        for m in range (len(colors)):
                            if (colors[m][1][0] > x) and\
                                 (colors[m][1][0] < (x+13)) and\
                                     (colors[m][1][1] > y) and\
                                         (colors[m][1][1] < (y+13)) and\
                                             (colors[m][1][2] > z) and\
                                                 (colors[m][1][2] < (z+13)) and\
                                                     (m not in used):
                                                    falsetot = falsetot + (colors[m][0]/pixmax)
                                                    used.append(m)
                        lengthlist.append(falsetot)



            
            
            '''
            colors = sorted(colors, key = lambda x:-x[0])
        
            for a in range (min(2000, len (colors))):
                col = matplotlib.colors.to_hex([ colors[a][1][0]/255, colors[a][1][1]/255, colors[a][1][2]/255 ])
                lengthlist.append(col)
            if len(colors)< 2000:
                for x in range (2000 - len(colors)):
                    lengthlist.append('#ffffff')
            '''
        
        print(n)

        n = n +1
        vectorlist.append(lengthlist)
    print(len(vectorlist))
    print(vectorlist[34])

    return vectorlist


def Write_up(vect):
    f= open("PreplanningCarrier.txt","w+")
    for x in range(len(vect)):    
        str1 = ''
        for y in range(len(vect[x])):
            str1 =  str1 + str(vect[x][y]) + ' '
        f.write("\r\n" + str1)
        print(x)
    f.close()
    return 


Write_up(preprocessing_logos())
