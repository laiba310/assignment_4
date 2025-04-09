import random 
num_sides=6
def main():
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    total: int = dice1 + dice2
    print(f"First die :{dice1}")
    print(f"Secound die :{dice2}")
    print("Total of two dice:", total)
    




if __name__ == '__main__':
    main()