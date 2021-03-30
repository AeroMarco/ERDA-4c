# WORK IN PROGRESS PROBABLY WILL BE SCRAPPED
# WORK IN PROGRESS PROBABLY WILL BE SCRAPPED
# WORK IN PROGRESS PROBABLY WILL BE SCRAPPED


import pygame 
from pygame.compat import bytes_
from pygame.pixelcopy import array_to_surface, surface_to_array, \
    map_array as pix_map_array, make_surface as pix_make_surface
import numpy 
from numpy import array as numpy_array, empty as numpy_empty, \
                  around as numpy_around, uint32 as numpy_uint32, \
                  ndarray as numpy_ndarray

numpy_floats = []
for type_name in "float float32 float64 float96".split():
    if hasattr(numpy, type_name):
        numpy_floats.append(getattr(numpy, type_name))

# Pixel sizes corresponding to NumPy supported integer sizes, and therefore
# permissible for 2D reference arrays.
_pixel2d_bitdepths = set([8, 16, 32])

'''next  2 functions Taken from 
pygame - Python Game Library
   Copyright (C) 2007 Marcus von Appen'
    This library is free software; you can redistribute it and/or
##    modify it under the terms of the GNU Library General Public
##    License as published by the Free Software Foundation; either
##    version 2 of the License, or (at your option) any later version.

'''
def blit_array (surface, array):
    """pygame.surfarray.blit_array(Surface, array): return None
    Blit directly from a array values.
    Directly copy values from an array into a Surface. This is faster than
    converting the array into a Surface and blitting. The array must be the
    same dimensions as the Surface and will completely replace all pixel
    values. Only integer, ascii character and record arrays are accepted.
    This function will temporarily lock the Surface as the new values are
    copied.
    """
    if isinstance(array, numpy_ndarray) and array.dtype in numpy_floats:
        array = array.round(0).astype(numpy_uint32)
    return array_to_surface(surface, array)

def array2d(surface):
    """pygame.numpyarray.array2d(Surface): return array
    copy pixels into a 2d array
    Copy the pixels from a Surface into a 2D array. The bit depth of the
    surface will control the size of the integer values, and will work
    for any type of pixel format.
    This function will temporarily lock the Surface as pixels are copied
    (see the Surface.lock - lock the Surface memory for pixel access
    method).
    """
    bpp = surface.get_bytesize()
    try:
        dtype = (numpy.uint8, numpy.uint16, numpy.int32, numpy.int32)[bpp - 1]
    except IndexError:
        raise ValueError("unsupported bit depth %i for 2D array" % (bpp * 8,))
    size = surface.get_size()
    array = numpy.empty(size, dtype)
    surface_to_array(array, surface)
    return array



Image = pygame.image.load('1.jpg')
reso =Image.get_rect().size

pygame.init()
print(reso)
'''
scr = pygame.display.set_mode(reso)
scr.blit(Image,(0,0))
pygame.display.update()

chad = array2d(scr)
chad2 = numpy.ones((len(chad),len(chad[0])))

#chad = np.linspace(1,3)
#pg.pixelcopy.surface_to_array(chad, scr)
#chad = pg.PixelArray(scr)
height = len(chad[0])
width = len(chad)
sortable = []
allowed = []
for x in range(round(width/4)):
    for y in range(round(height/4)):
        sortable.append(chad[x+ (round(width/4))][y+ (round(height/4))])
for x in sortable:
    if (x not in allowed) and (sortable.count(x) > 1000):
        allowed.append(x)
for x in range(width):
    for z in range (height):
        if (chad[x][z] in allowed):
            chad2[x][z] =  chad[x][z]
        else:
            chad2[x][z] = 0
        



blit_array(scr,chad2)
pygame.display.update()


'''

'''
print(len(chad[0]))
print(len(chad))
print(chad[0])

'''
