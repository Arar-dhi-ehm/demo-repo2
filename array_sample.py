import array as arr

numbers = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,])

# Print original array
print(f'\nOriginal: {numbers}')

# Changing first element
numbers[0] = -1
print(f'Change the first element: {numbers}')

# Get the last element
numbers[-1] = 20
print(f'Change the last element: {numbers}')

# Change 3rd to 5th element
numbers[2:5] = arr.array('i', [100, 101, 102])
print(f'Changing 3rd to 5th element: {numbers}')