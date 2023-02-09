"""
    Capabilities:
        Generate fake data
        Generate a localized fake data
        Useful for filling out forms using fake data
        Useful for volume tests
    Limitations:
        
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
    full_name = fake.name()
    first_name, last_name = full_name.split(" ")
    fake_email = f"{first_name.lower()}.{last_name.lower()}@samplemail.ph"
    print(f'\nFull Name: {full_name}')
    print(f'Email: {fake_email}')
    print(f'Phone Number: {fake.phone_number()}')
    print(f'Address: {fake.address()}')
    print(f'Job: {fake.job()}')
    print(f'Company: {fake.company()}')
    print(f'Birth Date: {fake.date_of_birth()}')



