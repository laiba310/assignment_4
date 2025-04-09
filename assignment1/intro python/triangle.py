def main():
    num1 = float(input("What is the length of side 1? "))
    num2 = float(input("What is the length of side 2? "))
    num3 = float(input("What is the length of side 3? "))

    perimeter = num1 + num2 + num3  # Renamed variable
    print(f"The perimeter of the triangle is {perimeter}.")

if __name__ == '__main__':
    main()
