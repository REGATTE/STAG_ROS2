import os
import tkinter.font as tkFont
from turtle import pen
from math import pi as PI
import cv2
from marker_generator.utils import Utils
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
        self.codeLocs = []
        self.nearbyCodes = []
        self.rad = 12
    
    def marker(self):  # sourcery skip: for-index-underscore
        self.initialise_component()

        self.markerSize = self.file_size / (1 + self.border_width * 2)
        self.borderSize = self.markerSize * self.border_width

        self.outerCircleDiameterSize = 2 * self.markerSize * self.outer_circle_radius
        self.innerCircleDiameterSize = 2 * self.markerSize * self.inner_circle_radius
        self.outerCircleTopLeft = (self.file_size - self.outerCircleDiameterSize)/2
        self.innerCircleTopLeft = (self.fileSize - self.innerCircleDiameterSize)/2
        self.codeCircleDiameterSize = 2 * self.innerCircleDiameterSize * self.code_Radius;
        self.fillerCircleDiameterSize = self.codeCircleDiameterSize * self.filler_Code_Radius;

        self.largeFont = tkFont.Font("Century Gothic", 72)
        self.smallFont = tkFont.Font("Century Gothic", 20)
        self.grayPen = pen(pencolor="grey", outline=3)

        self.fill_location()

        for self.HD in range(11, 23, 2):
            self.readCodeList()
            self.drawMarkers()
        
    def fill_location(self):
        for i in range(4):
            self.codeLocs.extend(
                (
                    Utils.polarToCart(
                        0.088363142525988, 0.785398163397448 + i * (PI / 2)
                    ),
                    Utils.polarToCart(
                        0.206935928182607, 0.459275804122858 + i * (PI / 2)
                    ),
                    Utils.polarToCart(
                        0.206935928182607, (PI/2) -  0.459275804122858 + i * (PI/2)
                    ),
                    Utils.polarToCart(
                        0.313672146827381, 0.200579720495241 + i * (PI / 2)
                    ),
                    Utils.polarToCart(
                        0.327493143484516, 0.591687617505840 + i * (PI / 2)
                    ),
                    Utils.polarToCart(
                        0.327493143484516, (PI / 2) - 0.591687617505840 + i * (PI / 2)
                    ),
                    Utils.polarToCart(
                        0.313672146827381, (PI / 2) - 0.200579720495241 + i * (PI / 2)
                    ),
                    Utils.polarToCart(
                        0.437421957035861, 0.145724938287167 + i * (PI / 2)
                    ),
                    Utils.polarToCart(
                        0.437226762361658, 0.433363129825345 + i * (PI / 2)
                    ),
                    Utils.polarToCart(
                        0.430628029742607, 0.785398163397448 + i * (PI / 2)
                    ),
                    Utils.polarToCart(
                        0.437226762361658, (PI / 2) - 0.433363129825345 + i * (PI / 2)
                    ),
                    Utils.polarToCart(
                        0.437421957035861, (PI / 2) - 0.145724938287167 + i * (PI / 2)
                    )
                )
            )
        for i in range(self.number_of_bits):
            self.nearbyCodes.append([])
            for j in range(self.number_of_bits):
                if i == j:
                    continue
                if Utils.distanceBetweenDoublePoints(self.codeLocs[i], self.codeLocs[j]) < self.code_radius * 4:
                    self.nearbyCodes[i].append(j)
        """ returning only to help with tests """
        return self.nearbyCodes

    def drawMarkers(self):
        os.chdir(os.getcwd())
        new_folders = f"HD{str(self.HD)}"
        os.makedirs(new_folders)

        # create a white bitmap image
        """
        Generate a bitmap

        Since python has no builtin bitmap function,
        I'm using a numpy array generate image.
        """
        img = Utils.createBitmapImage(self.file_size)

        for i in range(len(self.codes)):

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

            # Need to add smoothening filter - AntiAliasing

            """
            Apply Black Code Circles
            """
            for j in range(self.number_of_bits):
                if self.codes[i][j] == 1:
                    cv2.circle(
                        img,
                        [
                            Utils.centreCodeCircleX(j, self.innerCircleTopLeft, self.innerCircleDiameterSize, self.codeLocs),
                            Utils.centreCodeCircleY(j, self.innerCircleTopLeft, self.innerCircleDiameterSize, self.codeLocs)
                        ],
                        int(self.innerCircleDiameterSize/2),
                        (0,0,0),
                        -1
                    )
            """
            Apply Filler Circles
            """
            for j in range(self.number_of_bits):
                for k in range(self.number_of_bits):
                    if (self.codes[i][j] == 1) & (self.codes[i][k] == 1):
                        if k in self.nearbyCodes[j]:
                            cv2.circle(
                                img,
                                [
                                    Utils.centreFillerCircleX(j, k, self.innerCircleTopLeft, self.innerCircleDiameterSize, self.codeLocs),
                                    Utils.centreFillerCircleY(j, k, self.innerCircleTopLeft, self.innerCircleDiameterSize, self.codeLocs)
                                ],
                                int(self.fillerCircleDiameterSize/2),
                                (0,0,0),
                                -1
                            )
            """
            Apply White Code Circles
            """
            for j in range(self.number_of_bits):
                if self.codes[i][j] == 0:
                    cv2.circle(
                        img,
                        [
                            Utils.centreCodeCircleX(j, self.innerCircleTopLeft, self.innerCircleDiameterSize, self.codeLocs),
                            Utils.centreCodeCircleY(j, self.innerCircleTopLeft, self.innerCircleDiameterSize, self.codeLocs)
                        ],
                        int(self.innerCircleDiameterSize / 2),
                        (255, 255, 255),
                        -1
                    )
            """
            Erode & Dilate
            """


        

