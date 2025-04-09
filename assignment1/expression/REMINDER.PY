def main():
    
    dividend: int = int(input("Please enter an integer to be divided: "))
    divisor: int = int(input("Please enter an integer to divide by: "))

    q = dividend // divisor  
    r = dividend % divisor  
    
    print("The result of this division is " + str(q) + " with a remainder of " + str(r))



if __name__ == '__main__':
    main()
