## bw_Cons.py
##
## Written by Matthew Egan
## Last Revised: 25th June 2013

WIDTH_THRESHOLD = 1280
WIDTH_MEDIUM_THRESHOLD = 960

WIDTH_LARGE = 1280
HEIGHT_LARGE = 720

WIDTH_MEDIUM = 960
HEIGHT_MEDIUM = 540

WIDTH_SMALL = 640
HEIGHT_SMALL = 360

LRG_PADDING = 15
LRG_BTN_HEIGHT = 60

MED_PADDING = 11 ## 11.25 act.
MED_BTN_HEIGHT = 45

## Positions
ORIGIN = (0,0)
MED_TITLE_POS = (185, 30)
LRG_TITLE_POS = (250, 40)

## x = (ScreenWidth - ImgWidth)/2
LRG_LOGIN_POS = (445, 338)
LRG_CREATE_POS = (445, LRG_LOGIN_POS[1]+LRG_BTN_HEIGHT+LRG_PADDING)
LRG_LEADER_POS = (445, LRG_CREATE_POS[1]+LRG_BTN_HEIGHT+LRG_PADDING)
LRG_HELP_POS = (445, LRG_LEADER_POS[1]+LRG_BTN_HEIGHT+LRG_PADDING)
LRG_EXIT_POS = (445, LRG_HELP_POS[1]+LRG_BTN_HEIGHT+LRG_PADDING)

LRG_LOGIN_TITLE_POS = (451, 40)
LRG_LOGIN_USERNAME_POS = (545, LRG_LOGIN_POS[1]-LRG_BTN_HEIGHT-LRG_PADDING)
LRG_LOGIN_FIELD1_POS = (445, LRG_LOGIN_USERNAME_POS[1]+LRG_BTN_HEIGHT+LRG_PADDING)
LRG_LOGIN_PASSWORD_POS = (548, LRG_LOGIN_FIELD1_POS[1]+LRG_BTN_HEIGHT+LRG_PADDING)
LRG_LOGIN_FIELD2_POS = (445, LRG_LOGIN_PASSWORD_POS[1]+LRG_BTN_HEIGHT+LRG_PADDING)
LRG_LOGIN_CONFIRM_POS = (445, LRG_LOGIN_FIELD2_POS[1]+LRG_BTN_HEIGHT+LRG_PADDING)
LRG_LOGIN_EXIT_POS = (445, LRG_LOGIN_CONFIRM_POS[1]+LRG_BTN_HEIGHT+LRG_PADDING)

MED_LOGIN_POS = (334, 250)
MED_CREATE_POS = (334, MED_LOGIN_POS[1]+MED_BTN_HEIGHT+MED_PADDING)
MED_LEADER_POS = (334, MED_CREATE_POS[1]+MED_BTN_HEIGHT+MED_PADDING)
MED_EXIT_POS = (334, MED_LEADER_POS[1]+MED_BTN_HEIGHT+MED_PADDING)

# Screen Names
TITLE = "Title"
LOGIN = "Login"
NEWUSER = "NewUser"
HIGHSCORES = "HighScores"
HELP = "Help"
GAME = "Game"
EXITGAME = "Exit"