from math import sin, cos, sqrt
import numpy as np

class utils:
    def polarToCart(radius, radians):
        return(0.5 + cos(radians) * radius, 0.5 - sin(radians) * radius)
    def distanceBetweenDoublePoints(p1, p2):
        return sqrt((p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1]))
    def createIndexString(index):
        s = str(index)
        while(len(s) != len(str(codes))):
            s = "0" + s
        return s
    
    """
    Generate White color image
    """
    def createBitmapImage(value):
        new_image = np.zeros((value, value, 3), np.uint8)
        new_image[:]=(255,255,255)
        return new_image
        
