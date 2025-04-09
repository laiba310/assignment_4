import random

def hangman():
    # List of possible words to guess
    words = ['python', 'hangman', 'computer', 'developer', 'programming']

    # Randomly select a word
    word_to_guess = random.choice(words)

    # Create a list to store the current progress of the word (e.g., _ _ _ _ _)
    guessed_word = ['_'] * len(word_to_guess)

    # Set the number of allowed incorrect guesses
    attempts = 6

    # List to keep track of guessed letters
    guessed_letters = []

    print("🎯 Welcome to the Hangman Game!")

    while attempts > 0:
        print("\nCurrent Word:", ' '.join(guessed_word))
        print(f"Attempts remaining: {attempts}")
        print("Guessed letters:", guessed_letters)

        # Get the player's guess
        guess = input("Guess a letter: ").lower()

        # Ensure the guess is a valid letter
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter only one valid letter!")
            continue

        if guess in guessed_letters:
            print("❌ You've already guessed that letter!")
            continue

        # Add the guess to the guessed letters list
        guessed_letters.append(guess)

        # Check if the guess is in the word
        if guess in word_to_guess:
            print("✅ Correct guess!")

            # Reveal the guessed letter in the word
            for index in range(len(word_to_guess)):
                if word_to_guess[index] == guess:
                    guessed_word[index] = guess
        else:
            print("❌ Incorrect guess!")
            attempts -= 1

        # Check if the player has guessed the entire word
        if '_' not in guessed_word:
            print("\n🎉 Congratulations! You've guessed the word:", word_to_guess)
            break

    else:
        print("\n😞 You've lost! The word was:", word_to_guess)

# Call the function to play the game
hangman()
