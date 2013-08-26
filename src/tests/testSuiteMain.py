from testSuite import *

def main():
    print "--- Running Tests ---"

    print "    Beginning: checkLoginDriver"
    if checkLoginDriver():
        print "        checkLogin Passed!"
    else:
        print "        checkLogin Failed!"
    print "\n"

    print "    Beginning: checkValidUserDriver"
    if checkValidUserDriver():
        print "        checkValidUser Passed!"
    else:
        print "        checkValidUser Failed!"
    print "\n"

    print "    Beginning: storeNewUserDriver"
    if storeNewUserDriver():
        print "        storeNewUser Passed!"
    else:
        print "        storeNewUser Failed!"
    print "\n"

    print "    Beginning: readFileIntoArrayDriver"
    if readFileIntoArrayDriver():
        print "        readFileIntoArray Passed!"
    else:
        print "        readFileIntoArray Failed!"
    print "\n"

    print "    Beginning: sattoloShuffleDriver"
    if sattoloShuffleDriver():
        print "        sattoloShuffle Passed!"
    else:
        print "        sattoloShuffle Failed!"
    print "\n"

    print "    Beginning: submitScoreDriver"
    if submitScoreDriver():
        print "        submitScore Passed!"
    else:
        print "        submitScore Failed!"
    print "\n"

    print "    Beginning: sortAllTimeScoresDriver"
    if sortAllTimeScoresDriver():
        print "        sortAllTimeScores Passed!"
    else:
        print "        sortAllTimeScores Failed!"
    print "\n"

    print "    Beginning: sortDailyScoresDriver"
    if sortDailyScoresDriver():
        print "        sortDailyScores Passed!"
    else:
        print "        sortDailyScores Failed!"
    print "\n"

    print "--- Finished Tests ---"

if __name__ == "__main__": main()