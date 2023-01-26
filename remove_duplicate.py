"""
Remove duplicates from tuple using set.
"""

# Initialize tuple
sample_tuple = (1, 'Trafalgar', 5, 2, 3, 5, 1, 1, 3)

# Printing original tuple
print("\nThe original tuple is : " + str(sample_tuple))

# Removing duplicates from tuple using tuple() + set()
remove_duplicate = tuple(set(sample_tuple))

# Result
print(f"The tuple after removing duplicates : {str(remove_duplicate)}\n")

# Immutable check. Change value of Person Name
try:
    # Change tuple value: 'Trafalgar' into 'Law'
    sample_tuple[1] = 'Law'
except TypeError:
    print("\nYou can't change a tuple value because it is immutable (read-only).\n")