def loadWords():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


def getWordList(size):
    english_words = loadWords()

    return [word for word in english_words if len(word) == size]


def getNonGreenCharacterPositions(color):
    nonGreenCharacterPositions = []
    for i in range(len(color)):
        if color[i] != 'g':
            nonGreenCharacterPositions.append(i)

    return nonGreenCharacterPositions


def filterWordListFromCharacterColorConstraint(character, color, wordList, position, nonGreenCharacterPositions):

    filteredWordList = []

    if (color.lower() == 'g'):
        filteredWordList = [
            word for word in wordList if word[position] == character]

    elif (color.lower() == 'y'):
        for word in wordList:
            if (word[position] != character):
                for eachPosition in nonGreenCharacterPositions:
                    if (word[eachPosition] == character):
                        filteredWordList.append(word)
                        break

    else:
        for word in wordList:
            isCharacterFound = False
            for eachPosition in nonGreenCharacterPositions:
                if (word[eachPosition] == character):
                    isCharacterFound = True
                    break
            if not isCharacterFound:
                filteredWordList.append(word)

    return filteredWordList


def getNextPossibleWordList(word, color, nonGreenCharacterPositions, wordList=None):

    if (wordList is None):
        wordList = getWordList(len(word))

    for i in range(len(word)):
        wordList = filterWordListFromCharacterColorConstraint(
            word[i], color[i], wordList, i, nonGreenCharacterPositions)

    return wordList


wordList = []
print("Enter the number of character limit: ")
characterLimit = int(input())

for i in range(2, characterLimit+2):
    print("Enter the word number "+str((i-1)) + " : ", end='')
    word = input()

    print("Enter the color for word number " + str(i-1) + " : ", end='')
    color = input()

    nonGreenCharacterPositions = getNonGreenCharacterPositions(color)

    if (i == 2):
        wordList = getNextPossibleWordList(
            word=word, color=color, nonGreenCharacterPositions=nonGreenCharacterPositions)
    else:
        wordList = getNextPossibleWordList(
            word=word, color=color, nonGreenCharacterPositions=nonGreenCharacterPositions, wordList=wordList)

    print()
    print("Please choose any one word for the next attempt")
    print(wordList)

    if (len(wordList) <= 1):
        print("I hope you got the answer")
        break
