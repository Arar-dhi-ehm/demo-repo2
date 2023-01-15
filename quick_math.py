"""
    Capabilities:
        Calculate multiple numbers up to 99 using the same operators
        Calculate numbers using addition, subtraction, multiplication, division, modulo, and exponent
    Limitations:
        Can't use multiple operators at the same time
    Improvement:
        The '*' in multiplication and '**' in exponent is not working
"""

# import math
import sys

if len(sys.argv) < 4:
    print("Usage: quick_math.py <add|sub|mul|div|avg|pow> <num01> <num02> [num03..num99]")
    exit(1)

addition = {"+", "add", "addition", "plus"}
subtraction = {"-", "sub", "subtract", "subtraction", "minus"}
multiply = {"*", "x", "mul", "multiply"}
divide = {"/", "div", "divide"}
modulo = {"%", "avg", "average", "mod", "modulus", "modulo" }
exponent = {"**", "pow", "exponent"}

for counter in range(2, len(sys.argv)):
    if not sys.argv[counter].isdigit():
        print("Usage: quick_math.py <add|sub|mul|div|avg|pow> <num01> <num02> [num03..num99]")
        exit(1)

result = float(sys.argv[2])

if sys.argv[1] in addition:
    for counter in range(3, len(sys.argv)):
        result = result + float(sys.argv[counter])
elif sys.argv[1] in subtraction:
    for counter in range(3, len(sys.argv)):
        result = result - float(sys.argv[counter])
elif sys.argv[1] in multiply:
    for counter in range(3, len(sys.argv)):
        result = result * float(sys.argv[counter])
elif sys.argv[1] in divide:
    for counter in range(3, len(sys.argv)):
        result = result / float(sys.argv[counter])
elif sys.argv[1] in modulo:
    for counter in range(3, len(sys.argv)):
        result = result % float(sys.argv[counter])
elif sys.argv[1] in exponent:
    for counter in range(3, len(sys.argv)):
        result = result ** float(sys.argv[counter])
else:
    print("Usage: quickmath.py <add|mul|div|sub|avg|pow> <num01> <num02> [num03..num99]")
    exit(1)

print(f'\nResult: {result:,}\n')