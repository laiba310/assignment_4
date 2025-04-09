def in_range(n, low, high):
    return low <= n <= high

def main():
    num = int(input("Enter a number: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))
    
    if in_range(num, low, high):
        print(f"The number {num} is within the range of {low} and {high}.")
    else:
        print(f"The number {num} is outside the range of {low} and {high}.")

main()
