adult=18
def age_adult(age):
    if age>=adult:
        return True
    return False

def main():
    age=int(input("Enter your age:"))
    print(age_adult(age))
main()