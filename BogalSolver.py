import sys, random, string, time

rawBoard = ''
moves = 0
# size -> int
# generate board of size size x size filled with random chars
# @returns none
def generateBoard(size):
    outFile = 'test.txt'
    out = open(outFile, 'w')
    charlist = string.ascii_uppercase
    for z in range(0, size):
        line = ' '.join(random.choices(charlist, k=size))
        out.write((line + "\n"))
    out.close()
    return

# textFile -> string
# loads a board from a text file
# @returns board in 2D list form
def loadBoard(textFile):
    global rawBoard
    boardFile = open(textFile, 'r')
    rawBoard = boardFile.read().strip()
    n1 = rawBoard.count('\n') + 1
    n2 = rawBoard.count(' ') + n1
    assert n1**2 == n2
    # convert to 2-D array of chars
    board = rawBoard.replace(' ', '')
    board = board.split('\n')
    newBoard = []
    for i in range(0,len(board)):
        temp = board[i]
        newBoard += [list(temp)]
    boardFile.close()
    return newBoard

# board -> 2D array
# prints out the bogal board
def printBoard(board):
    print(rawBoard)

# coordinate -> list, board -> 2D list
# @returns list of all possible next positions
def possibleMoves(coordinate, board):
    possibleMoves = []
    #search for possible moves

    #try down move
    if coordinate[0] + 1 < len(board):
        possibleMoves.append([coordinate[0] + 1, coordinate[1]])

    # try up move
    if coordinate[0] - 1 > -1:
        possibleMoves.append([coordinate[0] - 1, coordinate[1]])

    #try right move
    if coordinate[1] + 1 < len(board):
        possibleMoves.append([coordinate[0], coordinate[1] + 1])

    # try left move
    if coordinate[1] - 1 > -1:
        possibleMoves.append([coordinate[0], coordinate[1] - 1])

    # try upper right corner move
    if coordinate[0] - 1 > -1 and coordinate[1] + 1 < len(board):
        possibleMoves.append([coordinate[0] - 1, coordinate[1] + 1])

    # try down right corner move
    if coordinate[0] + 1 < len(board) and coordinate[1] + 1 < len(board):
        possibleMoves.append([coordinate[0] + 1, coordinate[1] + 1])

    # try upper left corner move
    if coordinate[0] - 1 > -1 and coordinate[1] - 1 > -1:
        possibleMoves.append([coordinate[0] - 1, coordinate[1] - 1])

    # try down left corner move
    if coordinate[0]+1<len(board) and coordinate[1]-1>-1:
        possibleMoves.append([coordinate[0] + 1, coordinate[1] - 1])

    return possibleMoves

# possibleMoves -> 2D list, usedPath -> 2D list
# @returns the list of all legal moves
def legalMoves(possibleMoves, usedPath):
    moves = list(set(tuple(i) for i in possibleMoves) - set(tuple(j) for j in usedPath))
    return moves

# Function used for setting up all prefix dictionaries.
# This is not run with my program but was created because I'm lazy and
# didn't want to create the prefix dictionaries by hand.
def prefixDict():
    preFile = open('preDict.txt', 'w')
    preFile3 = open('preDict3.txt', 'w')
    preFile4 = open('preDict4.txt', 'w')
    preFile5 = open('preDict5.txt', 'w')
    dictFile = open('Dict.txt', 'r')
    preTxt = dictFile.read().split('\n')
    dictFile.close()
    txtSet = set()
    txtSet3 = set()
    txtSet4 = set()
    txtSet5 = set()
    for word in preTxt:
        txtSet.add(word[:2])
        txtSet3.add(word[:3])
        txtSet4.add(word[:4])
        txtSet5.add(word[:5])
    for word in txtSet:
        preFile.write(word)
        preFile.write('\n')
    for word in txtSet3:
        preFile3.write(word)
        preFile3.write('\n')
    for word in txtSet4:
        preFile4.write(word)
        preFile4.write('\n')
    for word in txtSet5:
        preFile5.write(word)
        preFile5.write('\n')

# board -> 2D list, currPos -> list, path -> 2D list
# boggle board, xy pair current position, path that got to that position
# @returns tuple of the word created and whether it is a real word.
def examineState(board, currPos, path, words, dict, preDict):
    global moves
    moves += 1
    path = path + [currPos]
    word = ''
    for i in range(0, len(path)):
        curr = path[i]
        word = (word + board[curr[0]][curr[1]]).lower()
    word = word[1:]
    if len(word) == 2:
       if word not in preDict[0]:
           return
    if len(word) == 3:
        if word not in preDict[1]:
            return
    if len(word) == 4:
        if word not in preDict[2]:
            return
    if len(word) == 5:
        if word not in preDict[3]:
            return
    # legalWord = (word, 'no')
    if word in dict:
       # legalWord = (word, 'yes')
        words.append(word)
    # if there is a legal move remaining, take it, otherwise return out of that level of recursion
    if legalMoves(possibleMoves(curr, board), path) != []:
        for i in range(0, len(legalMoves(possibleMoves(currPos, board), path))):
            examineState(board, legalMoves(possibleMoves(currPos, board), path)[i], path, words, dict, preDict)
        return words
    else:
        return words

def classifyWords(words):
    classWords = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for i in range(0, len(words)):
        lengthWord = len(words[i])
        classWords[lengthWord - 1].append(words[i])
    return classWords

def main():
    #prefixDict()
    prefixDictionary = [{},{},{},{},{}]
    # test run
    board = loadBoard('test.txt')
    # setup dictionaries from text files
    dictFile = open('Dict.txt', 'r')
    dict = set(dictFile.read().split('\n'))
    preDictFile = open('preDict.txt', 'r')
    prefixDictionary[0] = set(preDictFile.read().split('\n'))
    preDictFile3 = open('preDict3.txt', 'r')
    prefixDictionary[1] = set(preDictFile3.read().split('\n'))
    preDictFile4 = open('preDict4.txt', 'r')
    prefixDictionary[2] = set(preDictFile4.read().split('\n'))
    preDictFile5 = open('preDict5.txt', 'r')
    prefixDictionary[3] = set(preDictFile5.read().split('\n'))
    dictFile.close()
    print('OUPUT FROM FLINTSTONE CLASSIC BAM-BAM BASH-IT APPROACH:')
    printBoard(board)
    print("And we're off!")
    print('Running with cleverness ON')
    words = []
    startTime = time.time()
    for j in range(0,4):
         for i in range(0,4):
            words.extend(examineState(board, [i,j], [[i,j]], [], dict, prefixDictionary))
    endTime = time.time()
    searchTime = endTime - startTime

    print('All done\n')
    print('Searched total of ' + str(moves) + ' moves in ' + str(searchTime) + ' seconds\n')

    print('Words found: ')
    classifiedWords = classifyWords(words)
    for i in range(0, len(classifiedWords)):
        if classifiedWords[i] != []:
            print(str(i + 1) + ' -letter words: ' + str(classifiedWords[i]))
    print('\nFound ' + str(len(words)) + ' words total, ' + str(len(set(words))) + ' unique.')
    print('Alpha-sorted list of words:')
    print(str(sorted(words)))

if __name__ == "__main__":
    main()