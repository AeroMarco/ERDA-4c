import numpy as np
import codecs

import math
from PIL import Image

def preprocessing_type():  #this function does all the preprocessing for plane type recognition. It retuns a list of vecotors corresponding to the pictures in order form 1 to 100.
    
    n = 1
    n_pictures = 10 #number of pictures in dataset
    lengthlist = []
    vectorlist = []
    while n <= n_pictures: #for every picture



    
        #Alternate method using PIL
        
        img = Image.open(str(n)+'.jpg').convert('LA')
        new_img = img.resize((400,300))
        arra = np.array(new_img)
        #print(len(arra))
        #print(len(arra[0]))
        print(len(arra[0][0]))
        lengthlist = []
        for x in range (len(arra)):
            for y in range (len(arra[0])):
                if arra[x][y][0] > 210:
                    arra[x][y][0] = 1
                else: 
                    arra[x][y][0] = 0
        #print (arra[0])
        for x in range(len(arra)):
            for y in range(len(arra[x])):
                lengthlist.append(arra[x][y][0])
        vectorlist.append(lengthlist)
        n = n + 1
    
    return vectorlist

def Write_up(vect):
    f= open("Marco_planetype.txt","w+")
    for x in range(len(vect)):    
        str1 = ''
        for y in range(len(vect[x])):
            str1 =  str1 + str(vect[x][y]) + ' '
        f.write("\r\n" + str1)
    f.close()
    return 
Write_up(preprocessing_type())