"""
fruit_list.py
    Capabilities:
        - Gets a list from user input
        - Will remove duplicates from the list
        - Will sort the list alphabetically
        - The program will keep on asking until the user is done
        - Once the user completes their list, they can type 'exit' to stop the program

    Limitations:
        - Can't distinguish if user inputs a correct fruit name.
            - So if the user will input a float or integer it will still be added to the list
        - This program is case-sensitive, it will not be able to distinguish 'apple' from 'Apple'.
            - So if the user will input 'apple' and 'Apple', both items will be added in the list
        - Can't change or update the name of the fruit in the list
        - Can't delete a fruit in the list

    Work To Do:
        - If user will input an integer or float in the list, it must show an error
            - deferred
        - If the user entered a space, the space will be added into a list as string

    Sample of Fruit List:
        fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
"""


fruits = []
enter_fruit = ''
while enter_fruit != 'exit' and enter_fruit != 'EXIT':

    enter_fruit = input('\nPlease enter a fruit name to the list: \n>>> ')
    if enter_fruit != 'exit' and enter_fruit != 'EXIT':
        fruits.append(enter_fruit)
        fruits = list(dict.fromkeys(fruits))  # This will remove duplicates from the list

        print(f'\nFruits: {sorted(fruits)}')
        print(f'There are {len(fruits)} fruits in the list.')


