"""shell_calculator.py
    Capabilities:
        Can do simple calculator tasks
        Will keep on asking if the user will input invalid data
        Print exponent as superscript. Example Solution: 3⁵ = 243

    Limitations:
        One calculation at a time
        Only accept two integers
        
    Improvements:
        If the user just pressed enter in the 'Enter Choice' input, the app will crash
"""
import math

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def remainder(x, y):
    return x % y


# Function to convert to superscript
def get_super(convert):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    superscript = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = convert.maketrans(''.join(normal), ''.join(superscript))
    return convert.translate(res)


def power(x, y):
    return math.trunc(math.pow(x, y))


print('\nSelect Operation')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')
print('5. Modulus')
print('6. Power\n')


while True:
    # Take input from the user
    choice = input('Enter choice (1/2/3/4/5/6): ')

    # Check if choice is one of the 5 options
    if choice in ('1', '2', '3', '4', '5', '6',):
        num1 = float(input('\tEnter first number: '))
        num2 = float(input('\tEnter second number: '))

        if choice == '1':
            print(f'\t\tSolution: {num1:,} + {num2:,} = {add(num1, num2):,}\n')

        elif choice == '2':
            print(f'\t\tSolution: {num1:,} - {num2:,} = {subtract(num1, num2):,}\n')

        elif choice == '3':
            print(f'\tSolution: {num1:,} * {num2:,} = {multiply(num1, num2):,}\n')

        elif choice == '4':
            print(f'\tSolution: {num1:,} / {num2:,} = {divide(num1, num2):,}\n')

        elif choice == '5':
            print(f'\tSolution: {num1:,} % {num2:,} = {remainder(num1, num2):,}\n')
        
        elif choice == '6':
            # Print the power value (num2) as superscript
            print(f'\tSolution: {math.trunc(num1)}{get_super(str(math.trunc(num2)))} = {power(num1, num2):,}\n')

        # Check if the user wants another calculation. If 'no', break the loop.
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == 'no':
            print('\nGoodbye...\n')
            break

    else:
        print('\nSelect Operation')
        print('1. Add')
        print('2. Subtract')
        print('3. Multiply')
        print('4. Divide')
        print('5. Modulus')
        print('6. Power')
        print('\nInvalid Input: Please enter one of the choices: 1,2,3,4,5, or 6 only.\n')