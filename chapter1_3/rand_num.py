import random

def game():

    # generate random number between 1 & 20
    secret_num = int(input("Enter a number between 1 & 20 for me to guess: "))

    # computer guesses numbers to display to user    
    guess = random.randint(1, 20)            
    guesses = []

    while len(guesses) < 5:

        if guess==secret_num:
            print("Ya'ay! I got it. The number is {}".format(secret_num))
            break

        elif guess!=secret_num:

            # if it doesn't get correct answer in 1st attempt, it will ask for feedback
            # type "l" if your secret_num is less than computer's guess
            # type "h" if your secret_num is more than computer's guess

            print("Is it lower than or higher than {}".format(guess))
            user_input= input("")
            if user_input=="l":
                guess = random.randint(1, guess)
                print(guess)
            elif user_input=="h":
                guess = random.randint(guess, 20)
                print(guess)
        guesses.append(guess)

    else:
        print("I lost. Your number was: {}".format(secret_num))
game()