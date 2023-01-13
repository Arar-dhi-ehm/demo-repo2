"""
    Capabilities:
        Generate fake data
        Useful for filling out forms using fake data
    Prerequisites:
        pip install Faker
"""

from faker import Faker

fake = Faker()

# fake.add_provider(internet)
# print(fake.ipv4_private())

from faker import Faker
fake = Faker(['it_IT', 'en_US', 'en_CA', 'en_PH'])  # Localization
for _ in range(10):
    print(f'\nName: {fake.name()}')
    print(f'Phone Number: {fake.phone_number()}')
    print(f'Address: {fake.address()}')
    print(f'Job: {fake.job()}')
    print(f'Company: {fake.company()}')
    print(f'Birth Date: {fake.date_of_birth()}')



