def play_guessing_game(secret_number, attempts):
    print("Welcome to the Guessing Game!")
    print(f"Try to guess the secret number between 1 and 100. You have {attempts} attempts.")

    for attempt in range(1, attempts + 1):
        guess = int(input("Enter your guess number: "))
        
        if guess == secret_number:
            print("Congratulations! You guessed the secret number!")
            return
        elif guess < secret_number:
            print("Too low. Please try guess number.")
        else:
            print("Too high. please try guess number.")

    print("Sorry, you've run out of attempts. The secret number was:", secret_number)

play_guessing_game(secret_number=20, attempts=5)