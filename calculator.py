num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

s = '''
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Power
    6. Modulas
    7. Floor Division
    8. Exit
'''
while True:
    print(s)
    ch = int(input("Enter operation choice: "))

    match ch:
        case 1:
            print(addition(num1, num2))
        case 2:
            print(subtraction(num1, num2))
        case 3:
            print(multiplication(num1, num2))
        case 4:
            print(division(num1, num2))
        case 5:
            print(power(num1, num2))
        case 6:
            print(modulas(num1, num2))
        case 7:
            print(FloorDivision(num1, num2))
        case 8:
            break
        case _:
            print("Invalid Choice")