# The Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
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
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1 #.get() method, it searches for the specified key in the dictionary and 0 is the default value to be returned in case key is not found
    return freq
	
# -----------------------------------

# Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    freq_word = getFrequencyDict(word)
    score = 0
    for x in freq_word.keys():
        score = score + (freq_word[x]*SCRABBLE_LETTER_VALUES[x]) # This is under the assumption that scores will be counted for all the times an alphabet is used in the word
    score = score*len(word)
    if len(word)==n:
        score = score+50
    return score

#
# Displaying the hand
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line with a space in between each of the entries
    print()                             # print an empty line

#
# Dealing the Hand
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))] # The method randrange() returns a randomly selected element from range(start, stop, step), used for random subsetting
        hand[x] = hand.get(x, 0) + 1                # from consonants and vowels
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    word_dic = getFrequencyDict(word)
    copy_hand_dic = hand.copy()
    for x in word_dic.keys():
        if x in hand.keys():
            copy_hand_dic[x] = copy_hand_dic[x] - word_dic[x]
        else:
            copy_hand_dic = hand.copy() # This is to account for the fact if player tries to cheat by forming word out of alphabets absent from the dealt hand
            break
    return copy_hand_dic

#
# Testing word's validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # print("The dealt hand is: ",hand)
    # print("Word formed by the player is: ",word)
    if word=="":
        return False
    else:
        word_dic = getFrequencyDict(word)
        copy_hand_dic = hand.copy()
        for x in word_dic.keys():
            if x in hand.keys():
                copy_hand_dic[x] = copy_hand_dic[x] - word_dic[x]
            else:
                copy_hand_dic = hand.copy() # This is to account for the fact if player tries to cheat by forming word out of alphabets absent from the dealt hand
                break
        # print("The updated dictionary is: ",copy_hand_dic,"\n")
        if (min(copy_hand_dic.values())>=0) and (word in wordList) and copy_hand_dic!=hand:
            return True
        else:
            return False

#
# Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    return sum(hand.values())



def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    score = 0
    # As long as there are still letters left in the hand:
    while sum(hand.values())>0:
        # Display the hand
        displayHand(hand)
        # Ask user for input
        word = input("Enter word, or a ""."" to indicate that you are finished: ")
        # If the input is a single period:
            # End the game (break out of the loop)
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
        if word=="." or sum(hand.values())==0:
            print("Goodbye! Total score: " + str(score) + " points")
            break
    # Otherwise (the input is not a single period):
        # If the word is not valid:
            # Reject invalid word (print a message followed by a blank line)
        elif isValidWord(word,hand,wordList)==False:
            print("The entered word is invalid")
            print()
        # Otherwise (the word is valid):
            # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                # Update the hand 
        elif isValidWord(word,hand,wordList)==True:
            word_score = getWordScore(word, n)
            score = score + word_score
            print(word + " earned: " + str(word_score)+ " points. " + "Total: " + str(score) + " points")
            print()
            hand = updateHand(hand,word)

#
# Playing a game
# 

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    noh = 0 # noh - number of hands
    while True:
        n = random.randrange(8,20,1) # hand size i.e. in every turn a hand of size ranging from 8 to 20 shall be dealt
        sign = str(input("Enter n to deal a new hand, r to replay the last hand, or e to end game: "))
        if sign=="e":
            print("Game is Over")
            break
        elif sign=="n":
            Current_hand = dealHand(n)
            rev_hand = Current_hand.copy()
            playHand(Current_hand, wordList, n)
            noh=noh+1
        elif sign=="r" and noh>0:
            playHand(rev_hand, wordList, n)
            noh=noh+1
        while sign=="r" and noh==0:
            print("You have not played a hand yet. Please play a new hand first!" + "\n")
            sign = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        while sign not in ["n","r","e"]:
            print("Invalid command")
            sign = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        
            
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
