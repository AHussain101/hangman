
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist
def chooseWord(wordlist):
    return random.choice(wordlist)
wordlist = loadWords()
def isWordGuessed(secretWord, lettersGuessed):
    final= ''
    for i in secretWord:
        for letter in lettersGuessed:
          if i == letter:
            final += letter
    return secretWord == final
def getGuessedWord(secretWord, lettersGuessed):
    result = []
    for i in secretWord:
        if i in lettersGuessed:
            result.append(i)
        else:
            result.append('_')
    return ''.join(result)
def getAvailableLetters(lettersGuessed):
    string = "abcdefghijklmnopqrstuvwxyz"
    line = ""
    for i in string:
        if i not in lettersGuessed:
            line += i
    return line
def hangman(secretWord):
    print ("Welcome to the game, Hangman!")
    print ("I'm thinking of a word that is " + str(len(secretWord)) + " letters long.")
    lettersGuessed = ''
    guessesRemaining = 8
    print ("------------")
    while True:
        print ("You have " + str(guessesRemaining) + " guesses left.")
        print ("Available letters: " + getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ")
        if guess in secretWord and guess not in lettersGuessed:
            lettersGuessed += guess
            print ("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
        elif guess in lettersGuessed:
            print ("Oops u lol'ed! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed += guess
            print ("Sorry bro lol letter ain't in my word: " + getGuessedWord(secretWord, lettersGuessed))
            guessesRemaining -= 1
        print ("------------")
        if guessesRemaining <= 0:
            print ("Sorry!, You've ran out of guesses lol. The word was " + secretWord + ".")
            break
        if isWordGuessed(secretWord, lettersGuessed):
            print ("Congratulations homie! You've won!")
            break
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)

