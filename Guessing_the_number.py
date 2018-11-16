# Guessing the secret number between 0(closed) and 100(open)
print("Please think of a number between 0 and 100!")
low=0
high=100
guess = int((low+high)/2)
print("Is your secret number " + str(guess) + "?")
x = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly: ")
while True:
    if x in 'hlc':
        if x=='h':
            high = guess
        elif x=='l':
            low = guess
        else:
            print("Game over. Your secret number was: " + str(guess))
            break
        guess = int((low+high)/2)
        print("Is your secret number " + str(guess) + "?")
        x = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly: ")
    else:
      print("Sorry I didn't understand your input")
      print("Is your secret number " + str(guess) + "?")
      x = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly: ")  

    
    



