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

    global SIZE

    if dis.current_w > WIDTH_THRESHOLD:
        screenWidth = WIDTH_LARGE
        screenHeight = HEIGHT_LARGE
        SIZE = "L"
    elif dis.current_w > WIDTH_MEDIUM_THRESHOLD and dis.current_w <= WIDTH_THRESHOLD:
        screenWidth = WIDTH_MEDIUM
        screenHeight = HEIGHT_MEDIUM
        SIZE = "M"
    else: 
        screenWidth = WIDTH_SMALL
        screenHeight = HEIGHT_SMALL
        SIZE = "S"

    screen = pygame.display.set_mode((screenWidth, screenHeight))
    if not pygame.font: print "Warning: Font disabled"
    if not pygame.mixer: print "Warning: Sound disabled"
    pygame.display.set_caption("Battle Wizards")

    running = True
    currentScreen = "Title"
    # Application Loop
    while running:
        if currentScreen == "Title": displayTitleScreen(screen)
        elif currentScreen == "Login": pass
        elif currentScreen == "NewUser": pass
        elif currentScreen == "HighScores": pass
        elif currentScreen == "Help": pass
        elif currentScreen == "Game": pass
        elif currentScreen == "Exit": running = False
        pygame.display.update()

    print "END OF PROGRAM"

def displayTitleScreen(screen):
    # Event Loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    if SIZE == "L": bgImageSrc = "rsrc/largeBG.png"
    elif SIZE == "M": bgImageSrc = "rsrc/mediumBG.png"
    elif SIZE == "S": bgImageSrc = "rsrc/smallBG.png"

    # Load Images
    bgImage = pygame.image.load(bgImageSrc).convert_alpha() # Convert alpha since png is transparent

    screen.blit(bgImage, ORIGIN)

if __name__ == "__main__": main()
