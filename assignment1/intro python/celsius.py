def main():
    num=int(input("Enter temperature in Fahrenheit: "))
    degrees_celsius = (num - 32) * 5.0/9.0
    print(f"Temperature: {num} = {degrees_celsius}°C")
if __name__ == '__main__':
    main()