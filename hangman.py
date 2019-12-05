import time

name = input("What is your name? ")
print("Hello, " + name, "Time to play hangman!")

print("Start guessing...")

#choose the secret word
word = "code"

# creates an variable with an empty value
guesses = ''

#the number of tries
turns = 10

# Create a while loop

# check if the turns are more than zero
while turns > 0:

    # make a counter that starts with zero
    failed = 0

    # for every character in secret_word
    for char in word:

        # see if the character is in the players guess
        if char in guesses:

            # print then out the character
            print(char, )

        else:

            # if not found, print a dash
            print("_", )
            failed += 1

    if failed == 0:
        print("You won !")

        # exit the script
        break

    print()

    # ask the user go guess a character
    guess = input("guess a character:")

    #add the guess to guesses
    guesses += guess

    if guess not in word:

        #no. of turns will minus 1
        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Lose")