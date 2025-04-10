def main():
    while True:
        double = int(input("Enter your number: "))
        
        if double >= 100:
            print(f"We stop at {double} because that value is greater than or equal to 100.")
            break  
        
        result = double * 2
        print(f"{double} doubled is {result}")
        
main()
