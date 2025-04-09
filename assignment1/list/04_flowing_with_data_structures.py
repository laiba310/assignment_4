def add_three_copies(my_list, message):
    
    for _ in range(3):
        my_list.append(message)

def main():
   
    my_list = []
    
  
    message = input("Enter your word: ")

  
    print("List before:", my_list)

    add_three_copies(my_list, message)

    print("List after:", my_list)

main()
