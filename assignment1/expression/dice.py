import random 
num_sides=6
def roll_dice():
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    total: int = dice1 + dice2
    print("Total of two dice:", total)
    

def main():
    roll_dice1= 4

    roll_dice()
    roll_dice()
    roll_dice()

    print("die1 in main() is: " + str(roll_dice1))


if __name__ == '__main__':
    main()