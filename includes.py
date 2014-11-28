__author__ = 'brad'


import pygame
import random
import sys
import functions
import constants
from pygame.locals import *
from functions import *
from constants import *

pygame.init()

CARDFONT = pygame.font.SysFont("Arial", 12, True, False)
DISPLAYSURF = pygame.display.set_mode((640, 480))
BACKGROUND = pygame.image.load("sprites/felt.png")