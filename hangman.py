from wordGenerator import getHangmanWord

def hangman():
    print('Welcome to Hangman! \nThe rules are simple \nGuess the word \nYou only get so many chances before you lose \nGood Luck!')
    while True:
        try: 
            maxErrors = input(' Pick a number [1-10] for the amount of mistakes you may have: ')
            maxError = numberInputChecker(maxErrors)
            minCharacters = input('Pick a number [1-10] for minimum word length: ')
            minCharacter = numberInputChecker(minCharacters)
            break
        except (NameError, SyntaxError):
            print ('You must choose a number between 1 and 10 not a letter')
    currWord  = getHangmanWord(minCharacter)
    x = 0
    blanks = []
    while x < len(currWord)-1:
        blanks.append('_')
        x += 1
    print (blanks)
    print (maxError)
    print(currWord)
    print (len(currWord)-1)

def numberInputChecker(inputRecieved):
    if inputRecieved < 1 or inputRecieved > 10:
        print('Must be between 1 and 10')
        inputRecieved = input('Pick a number [1-10] for the amount of mistakes you may have: ')
        inputRecieved = numberInputChecker(inputRecieved)
        return (inputRecieved)
    else:
        return (inputRecieved)

hangman()
