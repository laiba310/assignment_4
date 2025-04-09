def guessing_game():
    secret_number = 20 
    attempts = 0  

    print("🎯 Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 20. Can you guess it?")

    while True:
        guess = int(input("Enter your guess: "))  
        attempts += 1  

        if guess > secret_number:
            print("📉 Too high! Try again.")
        elif guess < secret_number:
            print("📈 Too low! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed it right in {attempts} attempts.")
            break 

# Call the function to play the game
guessing_game()
