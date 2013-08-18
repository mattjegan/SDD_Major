import datetime

def readFileIntoArray(fileName):
    f = open(fileName)
    array = [line for line in f]
    f.close()
    return array

def submitScore(user, score, fileName):
    scoreFile = open(fileName, "a")
    
    # Get current date from OS
    today = datetime.date.today()
    date2rec = str(datetime.date.toordinal(today)) + ';\n'
    
    # Scores stored in format (user; score; date)
    scoreFile.write(str(user) + ';' + str(score) + ';' + str(date2rec))
    scoreFile.close()

def sortAllTimeScores(filename):
    arrayOfScores = readFileIntoArray(filename)
    for e, element in enumerate(arrayOfScores):
        # Split element into attributes - (UserWarning;score;timeAsOrdinal)
        arrayOfScores[e] = element.split(';')[:3]
    
    #for x in arrayOfScores:
    #    print x

    # Sort by score - decending
    arrayOfScores.sort(key=lambda x: int(x[1]))
    arrayOfScores.reverse()
    
    # Re-join all attributes into single element - 1D array of strings
    for e, element in enumerate(arrayOfScores):
        arrayOfScores[e] = ';'.join(element)
        arrayOfScores[e] = arrayOfScores[e] + ';\n'

    # Overwrite file
    fileToWrite = open(filename, "w+a")
    for element in arrayOfScores:
        fileToWrite.write(element)
    #fileToWrite.write('\n')
    fileToWrite.close()


import random
for i in xrange(10):
    submitScore("m", random.randint(0, 20), "allTime.txt")

x = raw_input("Waiting...")
sortAllTimeScores("allTime.txt")
