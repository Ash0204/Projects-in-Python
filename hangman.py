# Hangman game
# -----------------------------------
import string
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    count=0
    for letter in secretWord:
        if letter in lettersGuessed:
            count=count+1
    if count==len(secretWord):
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    secretwordlist = list(secretWord)
    for letter in secretwordlist:
        if letter not in lettersGuessed:
            secretwordlist[secretwordlist.index(letter)]='_'
    return " ".join(secretwordlist)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    complete_list = list(string.ascii_lowercase)
    for letter in complete_list:
        if letter in lettersGuessed:
            complete_list[complete_list.index(letter)]=""
    return "".join(complete_list) 
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    '''
    print("Welcome to the game, Hangman!" + "\n" + "I am thinking of a word that is " + str(len(secretWord)) + " letters long" + "\n" + "-------------")
    print("You have 8 guesses left." + "\n" + "Available letters: " + string.ascii_lowercase)
    nog = 8 #nog - number of guesses
    lettersGuessed = []
    available_letters = string.ascii_lowercase
    while nog>=1:
        guess = input("Please guess a letter: ")
        guess_lower = guess.lower()
        lettersGuessed.append(guess_lower)
        guessed_word = getGuessedWord(secretWord, lettersGuessed)
        if guess_lower in available_letters:
            if guess_lower in secretWord:
                print("Good guess: " + guessed_word + "\n" + "-------------")
            else:
                nog = nog-1
                print("Oops! That letter is not in my word: " + guessed_word + "\n" + "-------------")
        else:
            print("Oops! You've already guessed that letter: "+ guessed_word + "\n" + "-------------")
        if isWordGuessed(secretWord, lettersGuessed)==True:
            print("Congratulations, you won!")
            break
        elif nog==0 and isWordGuessed(secretWord, lettersGuessed)==False:
            print("Sorry, you ran out of guesses. The word was " + secretWord + ".")
            break
        available_letters=getAvailableLetters(lettersGuessed)
        print("You have " + str(nog) + " guesses left" + "\n" + "Available letters: " + available_letters)

# Playing the hangman game
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
