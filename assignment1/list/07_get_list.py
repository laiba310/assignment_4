def main():
    my_list = []
    
    while True:  
        user_input = input("Enter a number for the list (or press enter to stop): ")
        
        if user_input == "":  
            break  
        
        my_list.append(user_input)  
    
    print("Your list:", my_list)

main()
