from wordGenerator import getHangmanWord

def hangman():
    print('Welcome to Hangman! \nThe rules are simple \nGuess the word \nYou only get so many chances before you lose \nGood Luck!')
    maxErrors = input(' Pick a number [1-10] for the amount of mistakes you may have: ')
    maxError = numberInputChecker(maxErrors)
    minCharacters = input('Pick a number [1-10] for minimum word length: ')
    minCharacter = numberInputChecker(minCharacters)
    print (maxError)
    print (minCharacter)

def numberInputChecker(inputRecieved):
    inputRecieved = int(inputRecieved)
    if inputRecieved < 1 or inputRecieved > 10:
        print('Must be between 1 and 10')
        inputRecieved = input(' Pick a number [1-10] for the amount of mistakes you may have: ')
        inputRecieved = numberInputChecker(inputRecieved)
        return (inputRecieved)
    else:
        return (inputRecieved)

# hangman()
