"""Sample for random module
    Pick random number
    Pick random person
"""

import random

# Pick random number
random.random()  # returns a float between 0 to 1
random.randint(1, 6)  # returns an int between 1 to 6

# Pick random person
members = ['John', 'Bob', 'Mary']
leader = random.choice(members)  # randomly picks an item

print(leader)