from math import sin, cos, sqrt
import numpy as np

class Utils:
    def polarToCart(radius, radians):
        return(0.5 + cos(radians) * radius, 0.5 - sin(radians) * radius)
    def distanceBetweenDoublePoints(p1, p2):
        return sqrt((p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1]))
    
    """
    Generate White color image
    """
    def createBitmapImage(value):
        new_image = np.zeros((value, value, 3), np.uint8)
        new_image[:]=(255,255,255)
        return new_image
    def centreCodeCircleX(index_j, innerCircleTopLeft, innerCircleDiameterSize, list):
        return int(innerCircleTopLeft + innerCircleDiameterSize * list[index_j][0])/2
    def centreCodeCircleY(index_j, innerCircleTopLeft, innerCircleDiameterSize, list):
        return int(innerCircleTopLeft + innerCircleDiameterSize * list[index_j][1])/2
    def centreFillerCircleX(index_j, index_k, innerCircleTopLeft, innerCircleDiameterSize, list):
        return int(innerCircleTopLeft + innerCircleDiameterSize * ((list[index_j][0] + list[index_k][0]) / 2))
    def centreFillerCircleY(index_j, index_k, innerCircleTopLeft, innerCircleDiameterSize, list):
        return int(innerCircleTopLeft + innerCircleDiameterSize * ((list[index_j][1] + list[index_k][1]) / 2))

