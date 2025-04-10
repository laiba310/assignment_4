
def access_element(my_list, index):
    if 0 <= index < len(my_list):
        return f"Element at index {index} is: {my_list[index]}"
    else:
        return "Index out of range!"

def modify_element(my_list, index, new_value):
    if 0 <= index < len(my_list):
        my_list[index] = new_value
        return f"Updated list: {my_list}"
    else:
        return "Index out of range!"

def slice_list(my_list, start, end):
    if 0 <= start <= end <= len(my_list):
        return f"Sliced list: {my_list[start:end]}"
    else:
        return "Invalid slicing indices!"


def list_game():
    my_list = ['cat', 'dog', 'fish', 'bird', 'lion']  # Initial list
    print("Your starting list is:", my_list)

    while True:
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ").strip()
        
        if choice == '1':
            index = int(input("Enter index to access: "))
            print(access_element(my_list, index))

        elif choice == '2':
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            print(modify_element(my_list, index, new_value))

        elif choice == '3':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print(slice_list(my_list, start, end))

        elif choice == '4':
            print("Exiting the game. Bye!")
            break
        else:
            print("Invalid choice. Try again!")

list_game()
