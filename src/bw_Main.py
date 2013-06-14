## main.py
##
## Written by Matthew Egan
## Last Revision: 21st May 2013

import os
import sys
import time
import pygame
from bw_Cons import *
from pygame.locals import *

def main():
    pygame.init()

    dis = pygame.display.Info()
    print dis.current_w
    print dis.current_h

    if dis.current_w > WIDTH_THRESHOLD:
        screenWidth = WIDTH_LARGE
        screenHeight = HEIGHT_LARGE
    elif dis.current_w > WIDTH_MEDIUM_THRESHOLD and dis.current_w <= WIDTH_THRESHOLD:
        screenWidth = WIDTH_MEDIUM
        screenHeight = HEIGHT_MEDIUM
    else: 
        screenWidth = WIDTH_SMALL
        screenHeight = HEIGHT_SMALL

    screen = pygame.display.set_mode((screenWidth, screenHeight))
    if not pygame.font: print "Warning: Font disabled"
    if not pygame.mixer: print "Warning: Sound disabled"

    time.sleep(5)

    print "END OF PROGRAM"

if __name__ == "__main__": main()
