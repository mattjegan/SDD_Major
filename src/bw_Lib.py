## bw_Lib.py
##
## Written by Matthew Egan
## Last Revision: 14th June 2013

import os
import sys
import time
import pygame
from bw_Cons import *
from pygame.locals import *

def displayTitleScreen(screen, size):
    # Event Loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    if size == "L": bgImageSrc = "rsrc/largeBG.png"
    elif size == "M": bgImageSrc = "rsrc/mediumBG.png"
    elif size == "S": bgImageSrc = "rsrc/smallBG.png"

    # Load Images
    bgImage = pygame.image.load(bgImageSrc).convert_alpha() # Convert alpha since png is transparent

    screen.blit(bgImage, ORIGIN)
