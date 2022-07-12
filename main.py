import funcs as fn
import math

posGuesses = fn.get_guesses()
posWords = fn.get_words()

for word in posWords:
    if word not in posGuesses:
        posGuesses.append(word)

yellows = {1:[],2:[],3:[],4:[],5:[]}
greens = {1:'',2:'',3:'',4:'',5:''}
greys = []
greenlist = []
yellowlist = []

greensfound = False
yellowsfound = False

turn = 0

while True:
    if len(posWords) == 1:
        print("The word is", word + "!")
        break
    print(len(posGuesses), 'possible guesses')
    print(len(posWords), 'likely answers')
    if turn != 0:
        highestVal = -10000000000
        bestGuess = ''
        for guess in posGuesses:
            guessLetters = list(guess)
            greenCount = 0
            greyCount = 0
            yellowCount = 0
            for word in posWords:
                wordLetters = list(word)
                guessResult = ['','','','','']
                for i in range(5):
                    if guessLetters[i] == wordLetters[i]:
                        guessResult[i] = 'G'
                        greenCount = greenCount + 1
                        wordLetters[i] = ''
                    elif guessLetters[i] in wordLetters and guessLetters[i]:
                        guessResult[i] = 'Y'
                        yellowCount = yellowCount + 1
                        for x in range(5):
                            if wordLetters[x] == guessLetters[i]:
                                wordLetters[x] = ''
                                break
                    else:
                        guessResult[i] = 'X'
                        greyCount = greyCount + 1
            guessVal = greenCount + yellowCount - greyCount
            if guessVal > highestVal:
                bestGuess = guess
                highestVal = guessVal
    else:
        bestGuess = 'soare'
        highestVal = -619.0

    print(bestGuess, highestVal)

    num_greens = int(input("Number of greens: "))
    for i in range(num_greens):
        letter = input("Letter: ")
        space = int(input("Space (1-5): "))
        greens[space] = letter
        greenlist.append(letter)
        greensfound = True
    num_yellows = int(input("Number of yellows: "))
    for i in range(num_yellows):
        letter = input("Letter: ")
        space = int(input("Space (1-5): "))
        if letter not in yellows.keys():
            yellows[space] = [letter]
            yellowlist.append(letter)
        else:
            yellows[space].append(letter)
            yellowlist.append(letter)
        yellowsfound = True

    for letter in list(bestGuess):
        if letter not in greenlist and letter not in yellowlist:
            greys.append(letter)

    choiceWords = []
    for word in posGuesses:
        hasgrey = False
        hasgreens = False
        hasyellows = True
        for grey in greys:
            if grey in word:
                hasgrey = True
        if greensfound:
            for key in greens.keys():
                if greens[key]:
                    if list(word)[key-1] == greens[key]:
                        hasgreens = True
                    else:
                        hasgreens = False
                        break
        else:
            hasgreens = True

        yellowsinword = True
        if yellowsfound:
            for yellow in yellowlist:
                if yellow not in word:
                    yellowsinword = False
            if yellowsinword:
                for key in yellows.keys():
                    if yellows[key]:
                        for letter in yellows[key]:
                            if list(word)[key-1] == letter:
                                hasyellows = False
            else:
                hasyellows = False
        else:
            hasyellows = True
        if hasgreens and hasyellows and not hasgrey:
            choiceWords.append(word)

    newWords = []
    posGuesses.clear()
    for word in choiceWords:
        posGuesses.append(word)
        if word in posWords:
            newWords.append(word)
    posWords.clear()
    for word in newWords:
        posWords.append(word)

    print('-----')
    turn = turn + 1
