# simple calculator in python
choice = 0
while choice != 5:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter choice from 1 to 5:- "))

    if choice in range(1,4):
        a = float(input("Enter a No.:- "))
        b = float(input("Enter a No.:- "))

        if choice == 1:
            x = a + b
            print(f"Addition of {a} and {b} is {x} ")
        elif choice == 2:
            x = a - b
            print(f"Subtraction of {a} and {b} is {x} ")
        elif choice == 3:
            x = a * b
            print(f"Multiplication of {a} and {b} is {x} ")
        elif choice == 4:
            x = a / b
            print(f"Division of {a} and {b} is {x} ")
    elif choice == 5: 
        break
    else:
            print("Invalid choice please try again")