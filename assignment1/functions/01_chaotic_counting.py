import random

DONE_LIKELIHOOD = 0.3  # 30% chance to stop early

def done():
    # Return True with a likelihood defined by DONE_LIKELIHOOD
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    for i in range(1, 11):
        if done():
            return  # If done() returns True, stop the counting
        print(i, end=" ")
    print()

def main():
    chaotic_counting()
    print("I'm done.")

main()
