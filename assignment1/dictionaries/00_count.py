def main():
    number_counts = {}  # Empty dictionary to store counts

    while True:
        user_input = input("Enter a number (or press Enter to finish): ")
        if user_input == "":
            break  
        number = int(user_input)

        if number in number_counts:
            number_counts[number] += 1
        else:
            number_counts[number] = 1

    print("\nResult:")
    for number, count in number_counts.items():
        print(f"{number} appears {count} times.")

main()
