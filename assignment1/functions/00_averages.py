def find_average(num1, num2):
    average = (num1 + num2) / 2
    return average

def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = find_average(num1, num2)
    print(f"The average between {num1} and {num2} is: {result}")

main()
