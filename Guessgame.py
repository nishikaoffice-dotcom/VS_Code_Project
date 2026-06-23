
def Guessing_game_number():
    secret_number = 7
    Attempts = 0
    Guesses = None


    print("Welcome to the Number Guessing Game!")
    print("Already set the secret number")

# Loop until the player guesses correctly
    while Guesses != secret_number:
        Guesses = int(input("Please Guess any number : "))
        Attempts += 1

        if Guesses < secret_number:
            print("Guess was too low")
        elif Guesses > secret_number:
            print("Guess was too high")
        else:
            print(f"🎉 Congratulations! You guessed the number in {Attempts} attempts.") 

Guessing_game_number()

        







