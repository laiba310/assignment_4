import random

def random_choice():
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    attempt = 0

    print("🎮 Welcome to the Rock, Paper, Scissors Game!")

    while True:
        guess = input("Enter your choice (rock, paper, or scissors): ").lower().strip()
        attempt += 1

        if guess not in options:
            print("Invalid input. Try again.")
            continue

        print(f"Computer chose: {computer_choice}")

        if guess == computer_choice:
            print(f"🎉 It's a tie! You guessed it in {attempt} attempt(s).")
            break
        elif (guess == 'rock' and computer_choice == 'scissors') or \
             (guess == 'paper' and computer_choice == 'rock') or \
             (guess == 'scissors' and computer_choice == 'paper'):
            print(f"✅ You win! You beat the computer in {attempt} attempt(s).")
            break
        else:
            print("❌ You lose! Try again.")
            computer_choice = random.choice(options) 
random_choice()
