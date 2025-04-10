import random

def high_low():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')
    your_score = 0
    rounds = int(input("How many rounds would you like to play? "))
    
    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} ---")
        randomm = random.randint(1, 100)
        
        user = int(input("Enter your number: ")) 
        print(f"Your number is {user}")
       
        que = input("Do you think your number is higher or lower than the computer's? (Type 'higher' or 'lower'): ").strip().lower()

        if (user < randomm and que == 'lower') or (user > randomm and que == 'higher'):
            print(f"You were right! The computer's number was {randomm}")
            your_score += 1 
        else:
            print(f"Aww, that's incorrect. The computer's number was {randomm}")
    
    print("\nYour final score is", your_score)

    if your_score == rounds:
        print("Wow! You played perfectly! 🏆")
    elif your_score > rounds // 2:
        print("Good job, you played really well! 👍")
    else:
        print("Better luck next time! 😅")

high_low()
