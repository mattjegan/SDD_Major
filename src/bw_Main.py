## bw_Main.py
##
## Written by Matthew Egan
## Last Revision: 21st July 2013

import os
import sys
import time
import pygame
from bw_Cons import *
from bw_Lib import *
from pygame.locals import *

def main():
    pygame.init()

    dis = pygame.display.Info()
    print dis.current_w
    print dis.current_h

    size = "S"

    if dis.current_w > WIDTH_THRESHOLD:
        screenWidth = WIDTH_LARGE
        screenHeight = HEIGHT_LARGE
        size = "L"
    elif dis.current_w > WIDTH_MEDIUM_THRESHOLD and dis.current_w <= WIDTH_THRESHOLD:
        screenWidth = WIDTH_MEDIUM
        screenHeight = HEIGHT_MEDIUM
        size = "M"
    else: 
        screenWidth = WIDTH_SMALL
        screenHeight = HEIGHT_SMALL
        size = "S"

    screen = pygame.display.set_mode((screenWidth, screenHeight))
    if not pygame.font: print "Warning: Font disabled"
    if not pygame.mixer: print "Warning: Sound disabled"
    pygame.display.set_caption("Battle Wizards")

    running = True
    currentScreen = TITLE
    username = ""
    password = ""
    onUser = False
    onPass = False
    # Application Loop
    while running:
        if currentScreen == TITLE: currentScreen = displayTitleScreen(screen, size); username = ""; password = ""
        elif currentScreen == LOGIN: currentScreen, username, password, onUser, onPass = displayLoginScreen(screen, size, username, password, onUser, onPass)
        elif currentScreen == NEWUSER: currentScreen, username,password, onUser, onPass = displayNewUserScreen(screen, size, username, password, onUser, onPass)
        elif currentScreen == HIGHSCORES: 
            print HIGHSCORES
            break
        elif currentScreen == HELP: currentScreen = displayHelpScreen(screen, size)
        elif currentScreen == GAME: 
            print GAME
            break
        elif currentScreen == EXITGAME: running = False
        pygame.display.update()

    print "END OF PROGRAM"

if __name__ == "__main__": main()
