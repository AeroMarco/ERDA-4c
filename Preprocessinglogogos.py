#Get pixels of image
#make appropriate number of bins
#turn pixel color percentages into vector
#feed vector into ANN

from PIL import Image
import numpy as np
import codecs
import imagefuncts as imf
import math



def preprocessing_logos():  #this function does all the preprocessing for plane logo recognition. It retuns a list of vectors corresponding to the pictures in order form 1 to 100.
    
    n = 1
    n_pictures = 1 #number of pictures in dataset
    lengthlist = []
    vectorlist = []
    while n <= n_pictures: #for every picture
        
        img = Image.open(str(n)+'.jpg')
        new_img = img.resize((400,300))
        arra = np.array(new_img)

def Write_up(vect):
    f= open("PreplanningCarrier.txt","w+")
    for x in range(len(vect)):    
        str1 = ''
        for y in range(len(vect[x])):
            str1 =  str1 + str(vect[x][y]) + ' '
        f.write("\r\n" + str1)
    f.close()
    return 

