## bw_Main.py
##
## Written by Matthew Egan
## Last Revision: 26th August 2013

## Import all needed libraries

## Built-ins
import os
import sys
import time

## Externals
import pygame
from bw_Cons import *
from bw_Lib import *
from pygame.locals import *

## Main function for Battle Wizards Game
def main():
    ## Initialise PyGame Engine
    pygame.init()

    ## Set window dimensions
    screenWidth = WIDTH_LARGE
    screenHeight = HEIGHT_LARGE

    ## Create window
    screen = pygame.display.set_mode((screenWidth, screenHeight))

    ## Check if fonts and music works
    if not pygame.font: print "Warning: Font disabled"
    if not pygame.mixer: print "Warning: Sound disabled"

    ## Label the window
    pygame.display.set_caption("Battle Wizards")

    ## Initialise various values
    running = True
    currentScreen = TITLE
    username = ""
    password = ""
    onUser = False
    onPass = False
    hide = True
    
    ## Begin playing music
    pygame.mixer.init()
    pygame.mixer.music.load("rsrc/theme_song.mp3")
    
    ## Application Loop
    while running:

        ## Continue to play music
        if pygame.mixer.music.get_busy() != True:
            pygame.mixer.music.play()
        
        ## Determine the current screen to display
        if currentScreen == TITLE: currentScreen = displayTitleScreen(screen); username = ""; password = ""
        elif currentScreen == LOGIN: currentScreen, username, password, onUser, onPass, hide = displayLoginScreen(screen, username, password, onUser, onPass, hide)
        elif currentScreen == NEWUSER: currentScreen, username,password, onUser, onPass = displayNewUserScreen(screen, username, password, onUser, onPass)
        elif currentScreen == HIGHSCORES:
            ## Sort all scores before displaying 
            sortAllTimeScores("scores_alltime.txt")
            sortDailyScores("scores_alltime.txt", "scores_daily.txt")
            currentScreen = displayHighScores(screen)
        elif currentScreen == HELP: currentScreen = displayHelpScreen(screen)
        elif currentScreen == GAME: currentScreen = playGame(screen, username)
        elif currentScreen == EXITGAME: running = False

        ## Update screen
        pygame.display.update()

## Run main() function
if __name__ == "__main__": main()
