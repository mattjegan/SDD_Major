## bw_Cons.py
##
## Written by Matthew Egan
## Last Revised: 15th August 2013

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
LRG_USERNAME_START_POS = (LRG_LOGIN_FIELD1_POS[0] + LRG_PADDING, LRG_LOGIN_FIELD1_POS[1] + LRG_BTN_HEIGHT - (0.5*LRG_PADDING))
LRG_PASSWORD_START_POS = (LRG_LOGIN_FIELD2_POS[0] + LRG_PADDING, LRG_LOGIN_FIELD2_POS[1] + LRG_BTN_HEIGHT - (0.5*LRG_PADDING))

LRG_NEWUSER_TITLE_POS = (120, 54)

LRG_GAME_BAR = (ORIGIN[0], HEIGHT_LARGE-100)
LRG_GAME_TYPE = (ORIGIN[0]+10, HEIGHT_LARGE-90)
LRG_GAME_FIELD = (ORIGIN[0]+50+395, HEIGHT_LARGE-85)
LRG_GAME_CRTWORD = (LRG_LOGIN_PASSWORD_POS[0]-100, LRG_LOGIN_PASSWORD_POS[1] + 275)
LRG_GAME_CLOCK = (WIDTH_LARGE - 94-15, 15)

LRG_HELP_TITLE_POS = (495, LRG_LOGIN_TITLE_POS[1])
LRG_HELP_BODY_POS = (247, LRG_LOGIN_USERNAME_POS[1])
LRG_HELP_DONE_POS = LRG_LOGIN_CONFIRM_POS

LRG_STORE_BODY_POS = (247, LRG_LOGIN_USERNAME_POS[1]-40)
LRG_STORE_ATK_POS = (267, LRG_LOGIN_USERNAME_POS[1]+46)
LRG_STORE_ARR_POS = (267, LRG_LOGIN_USERNAME_POS[1]+(46*2)+15)
LRG_STORE_MAG_POS = (267, LRG_STORE_ARR_POS[1]+46+15)
LRG_PTNSLFT_POS = (700, LRG_STORE_ATK_POS[1])
LRG_ATK_PLS_POS = (600, LRG_STORE_ATK_POS[1])
LRG_ARR_PLS_POS = (600, LRG_STORE_ARR_POS[1])
LRG_MAG_PLS_POS = (600, LRG_STORE_MAG_POS[1])
LRG_STORE_DONE_POS = (LRG_HELP_DONE_POS[0], LRG_HELP_DONE_POS[1]-50)


MED_LOGIN_POS = (334, 250)
MED_CREATE_POS = (334, MED_LOGIN_POS[1]+MED_BTN_HEIGHT+MED_PADDING)
MED_LEADER_POS = (334, MED_CREATE_POS[1]+MED_BTN_HEIGHT+MED_PADDING)
MED_HELP_POS = (334, MED_LEADER_POS[1]+MED_BTN_HEIGHT+MED_PADDING)
MED_EXIT_POS = (334, MED_HELP_POS[1]+MED_BTN_HEIGHT+MED_PADDING)

MED_LOGIN_TITLE_POS = (451, 40)
MED_LOGIN_USERNAME_POS = (408, MED_LOGIN_POS[1]-MED_BTN_HEIGHT-MED_PADDING)
MED_LOGIN_FIELD1_POS = (334, MED_LOGIN_USERNAME_POS[1]+MED_BTN_HEIGHT+MED_PADDING)
MED_LOGIN_PASSWORD_POS = (410, MED_LOGIN_FIELD1_POS[1]+MED_BTN_HEIGHT+MED_PADDING)
MED_LOGIN_FIELD2_POS = (334, MED_LOGIN_PASSWORD_POS[1]+MED_BTN_HEIGHT+MED_PADDING)
MED_LOGIN_CONFIRM_POS = (334, MED_LOGIN_FIELD2_POS[1]+MED_BTN_HEIGHT+MED_PADDING)
MED_LOGIN_EXIT_POS = (334, MED_LOGIN_CONFIRM_POS[1]+MED_BTN_HEIGHT+MED_PADDING)
MED_USERNAME_START_POS = (MED_LOGIN_FIELD1_POS[0] + MED_PADDING, MED_LOGIN_FIELD1_POS[1] + MED_BTN_HEIGHT - (0.5*MED_PADDING))
MED_PASSWORD_START_POS = (MED_LOGIN_FIELD2_POS[0] + MED_PADDING, MED_LOGIN_FIELD2_POS[1] + MED_BTN_HEIGHT - (0.5*MED_PADDING))

MED_NEWUSER_TITLE_POS = (90, 40)

MED_HELP_TITLE_POS = (355, MED_LOGIN_TITLE_POS[1])
MED_HELP_BODY_POS = (144, MED_LOGIN_USERNAME_POS[1])
MED_HELP_DONE_POS = MED_LOGIN_CONFIRM_POS

# Screen Names
TITLE = "Title"
LOGIN = "Login"
NEWUSER = "NewUser"
HIGHSCORES = "HighScores"
HELP = "Help"
GAME = "Game"
EXITGAME = "Exit"
