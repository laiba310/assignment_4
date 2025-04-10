import random

def user_binary_guess_game():
    print("🎯 Welcome to the Binary Search Guessing Game!")
    
    # Step 1: Sorted list
    numbers = list(range(1, 20))  # 1 se 100 tak numbers
    target = random.choice(numbers)  # 🎯 Computer ne number chhupa liya

    print("🤖 I have selected a number between 1 and 20.")
    print("🧠 Try to find it using binary search logic!")
    
    attempts = 0

    low = 0
    high = len(numbers) - 1

    while True:
        try:
            guess = int(input("🔢 Your guess: "))
        except ValueError:
            print("🚫 Invalid input. Please enter a number.")
            continue

        attempts += 1

        if guess == target:
            print(f"🎉 Correct! You found the number {target} in {attempts} tries.")
            break
        elif guess < target:
            print("🔼 Too low! Try a higher number.")
            low = guess + 1
        else:
            print("🔽 Too high! Try a lower number.")
            high = guess - 1

        print(f"📉 Your current range: {low + 1} to {high + 1}")

# Run the game
user_binary_guess_game()
