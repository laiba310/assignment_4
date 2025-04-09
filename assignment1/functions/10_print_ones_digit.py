def print_ones_digit(num):
    print("The ones digit is", num % 10)

def main():
    number = int(input("Enter a number: "))
    print_ones_digit(number)

main()
