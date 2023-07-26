import os, sys
import tkinter.font as tkFont
from turtle import pen
from math import pi as PI

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
    
    def marker(self):  # sourcery skip: for-index-underscore
        self.initialise_component()

        markerSize = self.file_size / (1 + self.border_width * 2)
        borderSize = markerSize * self.border_width

        outerCircleDiameterSize = 2 * markerSize * self.outer_circle_radius
        innerCircleDiameterSize = 2 * markerSize * self.inner_circle_radius
        outerCircleTopLeft = (self.file_size - outerCircleDiameterSize)/2
        innerCircleTopLeft = (self.fileSize - innerCircleDiameterSize)/2
        codeCircleDiameterSize = 2 * innerCircleDiameterSize * self.code_Radius;
        fillerCircleDiameterSize = codeCircleDiameterSize * self.filler_Code_Radius;

        largeFont = tkFont.Font("Century Gothic", 72)
        smallFont = tkFont.Font("Century Gothic", 20)
        grayPen = pen(pencolor="grey", outline=3)

        self.fill_location()

        for HD in range(11, 23, 2):
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

    def initialise_component(self):
    def readCodeList(self):
    def drawMarkers(self):
