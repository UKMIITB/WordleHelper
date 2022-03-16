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


def getSuggestionResult(guess_word, guess_word_result, iteration, word_list=None):

    nonGreenCharacterPositions = getNonGreenCharacterPositions(
        guess_word_result)

    if (iteration == 1):
        word_list = getWordList(len(guess_word))

    for i in range(len(guess_word)):
        word_list = filterWordListFromCharacterColorConstraint(
            guess_word[i], guess_word_result[i], word_list, i, nonGreenCharacterPositions)

    word_list.sort()

    return word_list
