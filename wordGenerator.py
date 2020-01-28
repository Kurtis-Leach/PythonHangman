import random
# words = open("words.txt", 'r') 
# returnedWords = words.read()
# print(returnedWords)
# file1 = open("words.txt","w") 
# L = ["Banana\n","Horse\n","Super\n","Puzzle\n","Dictionary\n","Free\n","Cellular\n","Kurtis\n","Brianna\n","Netflix\n"]   
# file1.writelines(L) 
# file1.close() #to change file acc


def getHangmanWord(minCharcters):
    wordsProcessed = 0
    currWord = None
    with open('words.txt','r') as f:
        for word in f:
            if '(' in word or ')' in word:
                continue
            if len(word) < minCharcters:
                continue
            wordsProcessed += 1
            if random.randint(1, wordsProcessed) == 1:
                currWord = word
    return (currWord)