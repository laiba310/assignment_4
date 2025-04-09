def count_even(lst):
    even_count = 0
    
    for num in lst:
        if num % 2 == 0:
            even_count += 1
    
    print(f"There are {even_count} even numbers in the list.")

def main():
    lst = []
    
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        
        if user_input == "":
            break
        
        num = int(user_input)
        lst.append(num)
    
    count_even(lst)

main()
