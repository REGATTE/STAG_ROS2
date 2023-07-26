from math import sin, cos, sqrt

class utils:
    def polarToCart(radius, radians):
        return(0.5 + cos(radians) * radius, 0.5 - sin(radians) * radius)
    def distanceBetweenDoublePoints(p1, p2):
        return sqrt((p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1]))