print("Please think of a number between 0 and 100!")

# At the start the highest the number could be is 100 and the lowest is 0.
hi = 100
lo = 0
guessed = False

# Loop until we guess it correctly
while not guessed:
    # Bisection search: guess the midpoint between our current high and low guesses
    guess = (hi + lo)/2
    print("\nIs your secret number " + str(guess)+ "?")
    user_inp = raw_input("\nEnter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if user_inp == 'c':
        # We got it right!
        guessed = True
    elif user_inp == 'h':
        # Guess was too high. So make the current guess the highest possible guess.
        hi = guess-1
    elif user_inp == 'l':
        # Guess was too low. So make the current guess the lowest possible guess.
        lo = guess+1
    else:
        print("\nSorry I did not understand your input.")

print('\nGame over. Your secret number was: ' + str(guess))
