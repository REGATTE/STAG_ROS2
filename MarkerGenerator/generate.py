import os, sys
import tkinter.font as tkFont
from turtle import pen
from math import pi as PI

from PIL import Image
import cv2

from utils import *

class Generate():
    def __init__(self):
        super().__init__('generate')
        self.number_of_bits = 48
        self.border_width = 0.125
        self.outer_circle_radius = 0.4
        self.inner_circle_radius = 0.35
        self.code_radius = 0.062482177287080
        self.filler_code_radius = 0.7
        self.file_size = 1000
        self.codes = []
    
    def marker(self):  # sourcery skip: for-index-underscore
        self.initialise_component()

        self.markerSize = self.file_size / (1 + self.border_width * 2)
        self.borderSize = self.markerSize * self.border_width

        outerCircleDiameterSize = 2 * self.markerSize * self.outer_circle_radius
        innerCircleDiameterSize = 2 * self.markerSize * self.inner_circle_radius
        outerCircleTopLeft = (self.file_size - outerCircleDiameterSize)/2
        innerCircleTopLeft = (self.fileSize - innerCircleDiameterSize)/2
        codeCircleDiameterSize = 2 * innerCircleDiameterSize * self.code_Radius;
        fillerCircleDiameterSize = codeCircleDiameterSize * self.filler_Code_Radius;

        largeFont = tkFont.Font("Century Gothic", 72)
        smallFont = tkFont.Font("Century Gothic", 20)
        grayPen = pen(pencolor="grey", outline=3)

        self.fill_location()

        for self.HD in range(11, 23, 2):
            self.readCodeList()
            self.drawMarkers()
        
    def fill_location(self):
        codeLocs = []
        for i in range(4):
            codeLocs.extend(
                (
                    utils.polarToCart(
                        0.088363142525988, 0.785398163397448 + i * (PI / 2)
                    ),
                    utils.polarToCart(
                        0.206935928182607, 0.459275804122858 + i * (PI / 2)
                    ),
                    utils.polarToCart(
                        0.206935928182607, (PI/2) -  0.459275804122858 + i * (PI/2)
                    ),
                    utils.polarToCart(
                        0.313672146827381, 0.200579720495241 + i * (PI / 2)
                    ),
                    utils.polarToCart(
                        0.327493143484516, 0.591687617505840 + i * (PI / 2)
                    ),
                    utils.polarToCart(
                        0.327493143484516, (PI / 2) - 0.591687617505840 + i * (PI / 2)
                    ),
                    utils.polarToCart(
                        0.313672146827381, (PI / 2) - 0.200579720495241 + i * (PI / 2)
                    ),
                    utils.polarToCart(
                        0.437421957035861, 0.145724938287167 + i * (PI / 2)
                    ),
                    utils.polarToCart(
                        0.437226762361658, 0.433363129825345 + i * (PI / 2)
                    ),
                    utils.polarToCart(
                        0.430628029742607, 0.785398163397448 + i * (PI / 2)
                    ),
                    utils.polarToCart(
                        0.437226762361658, (PI / 2) - 0.433363129825345 + i * (PI / 2)
                    ),
                    utils.polarToCart(
                        0.437421957035861, (PI / 2) - 0.145724938287167 + i * (PI / 2)
                    )
                )
            )
        nearbyCodes = []
        for i in range(self.number_of_bits):
            nearbyCodes.append([])
            for j in range(self.number_of_bits):
                if i == j:
                    continue
                if utils.distanceBetweenDoublePoints(codeLocs[i], codeLocs[j]) < self.code_radius * 4:
                    nearbyCodes[i].append(j)

    def drawMarkers(self):
        os.chdir(os.getcwd)
        new_folders = f"HD{str(self.HD)}"
        os.makedirs(new_folders)

        # create a white bitmap image
        """
        Generate a bitmap

        Since python has no builtin bitmap function,
        I'm using a numpy array generate image.
        """
        img = utils.createBitmapImage(self.file_size)

        for i in range(i < self.codes):

            # Draw Outer Rectangle 
            """
            Draw outer rectangle.
            -1 added to cv2.rectangle to fill rectangle with the specified color
            """
            cv2.rectangle(img, [int(self.borderSize), int(self.borderSize)], [int(self.borderSize + self.markerSize), int(self.borderSize + self.markerSize)], (0,0,0), -1)
            """
            Draw Outer Circle
            -1 added to cv2.circle to fill circle with the specified color
            """
            cv2.circle(img, (500, 500), int(self.outerCircleDiameterSize/2), (255,255,255), -1)

            """
            Draw Inner Circles
            """
            for j in range(self.number_of_bits):
                if(self.codes[i][j] == 1):
                    cv2.circle(img, )


        

