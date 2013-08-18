def readFileIntoArray(fileName):
    f = open(fileName)
    array = [line for line in f]
    f.close()
    return array

def sortAllTimeScores(filename):
    arrayOfScores = readFileIntoArray(filename)
    for e, element in enumerate(arrayOfScores):
        # Split element into attributes - (UserWarning;score;timeAsOrdinal)
        arrayOfScores[e] = element.split(';')[:3]
    
    # Sort by score - decending
    arrayOfScores.sort(key=lambda x: x[1])
    arrayOfScores.reverse()
    
    # Re-join all attributes into single element - 1D array of strings
    for e, element in enumerate(arrayOfScores):
        arrayOfScores[e] = ';'.join(element)

    # Overwrite file
    fileToWrite = open(filename, "w")
    for element in arrayOfScores:
        fileToWrite.write(element)
    fileToWrite.close()

sortAllTimeScores("allTime.txt")
