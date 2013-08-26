from bw_Lib import *

def checkLoginDriver():
    try:
        assert(checkLogin("matthew", "egannn") == True)
        assert(checkLogin("egannn", "matthew") == False)
        return True
    except:
        return False

def checkValidUserDriver():
    try:
        assert(checkValidUser("matthew", "egannn") == True)
        assert(checkValidUser("matt", "egan") != True)
        assert(checkValidUser("", "") != True)
        return True
    except:
        return False

def storeNewUserDriver():
    storeNewUser("dogdog", "catcat")
    storeNewUser("marrio", "luiggi")
    print "MUST DO: Examine userFile.txt"
    print "         confirm the following contents:"
    print "         matthew;egannn"
    print "         dogdog;catcat"
    print "         marrio;luiggi"
    if raw_input("Y/N? ") == ("Y" or "y"):
        return True
    else:
        return False

def readFileIntoArrayDriver():
    try:
        assert(readFileIntoArray("wordList.txt") == ["cat\r\n", "dog\r\n", "unicorn\r\n", "horse"])
        assert(readFileIntoArray("empty.txt") == [])
        assert(readFileIntoArray("nonExistent.txt") == None)
        return True
    except:
        return False

def sattoloShuffleDriver():
    try:
        assert(sattoloShuffle([1, 2, 3, 4, 5]) != [1, 2, 3, 4, 5])
        assert(sattoloShuffle(["a", "b", "c", "d", "e"]) != ["a", "b", "c", "d", "e"])
        return True
    except:
        return False

def submitScoreDriver():
    submitScore("matthew", 10, "scores_alltime.txt")
    submitScore("matthew", 12, "scores_alltime.txt")
    submitScore("marrio", -1, "scores_alltime.txt")
    print "MUST DO: Examine scores_alltime.txt"
    print "         confirm the following contents:"
    print "         matthew;10;xxxxxx"
    print "         matthew;12;xxxxxx"
    print "         marrio;-1;xxxxxx"
    if raw_input("Y/N? ") == ("Y" or "y"):
        return True
    else:
        return False

def sortAllTimeScoresDriver():
    sortAllTimeScores("scores_alltime.txt")
    print "MUST DO: Examin scores_alltime.txt"
    print "         confirm the following contents:"
    print "         matthew;12;xxxxxx"
    print "         matthew;10;xxxxxx"
    print "         marrio;-1;xxxxxx"
    if raw_input("Y/N? ") == ("Y" or "y"):
        return True
    else:
        return False

def sortDailyScoresDriver():
    sortDailyScores("scores_daily.txt")
    print "MUST DO: Examin scores_alltime.txt"
    print "         confirm the following contents:"
    print "         matthew;12;xxxxxx"
    print "         matthew;10;xxxxxx"
    print "         marrio;-1;xxxxxx"
    if raw_input("Y/N? ") == ("Y" or "y"):
        return True
    else:
        return False