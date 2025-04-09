def main():
    C = 299792458 
    m=float(input("Enter kilos of mass: "))
    E=m * (C ** 2)
    print("e = m * C^2...")
    print(f"m = {m} kg")
    print(f"C= {C} m/s")
    
    print(f"{E}e joules of energy!")
if __name__ == '__main__':
    main()