def get_first_element(lst):
    print(lst[-1])

def main():
    my_list = []
    for i in range(3):
        user = input("Enter a number for the list: ")
        my_list.append(int(user))
    get_first_element(my_list)

main()
