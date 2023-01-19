import getpass

database = {'user1': 'pass123', 'user2': 'pass456'}
username = input('Enter first name: ')
password = getpass.getpass('Enter password: ')
try:
    for user in database.keys():
        if username == user:
            while password != database.get(user):
                wrong_password = getpass.getpass('Enter you password again: ')
            break
except Exception as e:
    print(e)

print('Verified')