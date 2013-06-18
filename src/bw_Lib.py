## bw_Lib.py
##
## Written by Matthew Egan
## Last Revision: 18th June 2013

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
        elif event.type = MOUSEBUTTONDOWN:
            pass
    
    if size == "L": 
        bgImageSrc = "rsrc/large/title_BG.png"
        bwTextSrc = "rsrc/large/title_Text.png"
    elif size == "M":
        bgImageSrc = "rsrc/medium/title_BG.png"
        bwTextSrc = "rsrc/medium/title_Text.png"
        loginSrc = "rsrc/medium/title_Login.png"
        createSrc = "rsrc/medium/title_CreateAcc.png"
        leaderSrc = "rsrc/medium/title_Leaderboards.png"
        exitSrc = "rsrc/medium/title_Exit.png"
    elif size == "S": 
        bgImageSrc = "rsrc/smallBG.png"

    # Load Images
    bgImage = pygame.image.load(bgImageSrc).convert_alpha() # Convert alpha since png is transparent
    bwText = pygame.image.load(bwTextSrc).convert_alpha()
    loginImg = pygame.image.load(loginSrc).convert_alpha()
    createImg = pygame.image.load(createSrc).convert_alpha() 
    leaderImg = pygame.image.load(leaderSrc).convert_alpha()
    exitImg = pygame.image.load(exitSrc).convert_alpha()

    screen.blit(bgImage, ORIGIN)

    if size == "L":
        screen.blit(bwText, LRG_TITLE_POS)
    elif size == "M":
        screen.blit(bwText, MED_TITLE_POS)
        screen.blit(loginImg, MED_LOGIN_POS)
        screen.blit(createImg, MED_CREATE_POS)
        screen.blit(leaderImg, MED_LEADER_POS)
        screen.blit(exitImg, MED_EXIT_POS)
    elif size == "S":
        pass