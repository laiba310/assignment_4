AFFIRMATION  = "I am capable of doing anything I put my mind to."

def main():
    print(F"Please type the following affirmation: {AFFIRMATION}")

    user = input()  
    while user != AFFIRMATION:  
        print("That was not the affirmation.")

        
        print(f"Please type the following affirmation: {AFFIRMATION} ")
        user = input()

    print("That's right! :)")


    main()