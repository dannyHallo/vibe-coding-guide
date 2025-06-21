def add(x, y):
    """This function adds two numbers"""
    return x + y

def main():
    """Main function to run the calculator"""
    print("Add two numbers.")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        print(f"{num1} + {num2} = {add(num1, num2)}")
        
        next_calculation = input("Let's do another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
