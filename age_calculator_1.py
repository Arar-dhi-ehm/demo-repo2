"""age_calculator_1.py

This is the OOP version of age_calculator.py
"""


class AgeCalculator:
    def __init__(self, name, birth_month, birth_year):
        self.name = name
        self.birth_month = birth_month
        self.birth_year = birth_year

    def calculate_age(self):
        age = 2022 - self.birth_year
        return age

    def calculate_decades(self):
        age = self.calculate_age()
        decades = float(age / 10)
        return decades

    def get_comment(self):
        age = self.calculate_age()
        if age < -1:
            return 'You are not yet born in this world.'
        elif age < 1:
            return 'You must still be inside your mom\'s womb.'
        elif age < 20:
            return 'So you\'re in college? Focus on the future ahead of you! Go all out!'
        elif age < 25:
            return 'Time goes by quickly. Go travel!'
        elif age < 30:
            return 'Keep hustling! Never stop learning!'
        elif age < 50:
            return 'Are you near retirement? Don\'t overdo it.'
        elif age < 70:
            return 'You should relax and retire.'
        elif age < 80:
            return 'Did you know that you are born within the time of World War II?'
        elif age < 90:
            return 'Did you know that you are born after World War II? You must have a hard time.'
        elif age < 135:
            return 'You might have known Adolf Hitler of Germany?'
        elif age < 250:
            return 'You might have known Charles Darwin, the mind behind influential theory of evolution?'
        elif age < 500:
            return 'You might have known Galileo Galilei, the father of modern science?'
        elif age < 600:
            return 'You might have known Leonardo da Vinci of the Italian Renaissance?'
        elif age < 700:
            return 'Wow! You got a legendary record! What\'s your secret?'
        elif age < 1000:
            return 'You might have known Genghis Khan, the warrior who founded the first Mongol Empire?'
        elif age < 2000:
            return 'This is majestic! You\'re a mythical legend!'
        elif age < 2170:
            return 'You might have known Julius Caesar of the Roman Empire?'
        elif age < 2380:
            return 'You might have known Alexander the Great of Macedonia?'
        elif age < 2450:
            return 'You might have known Plato the influential philosopher?'
        else:
            return 'I can\'t believe it! Are you immortal?'

    def get_zodiac_sign(self):
        if self.birth_month == 'January':
            return 'Your zodiac sign might be Capricorn or Aquarius.'
        elif self.birth_month == 'February':
            return 'Your zodiac sign might be Aquarius or Pisces.'
        elif birth_month == 'March':
            return 'Your zodiac sign might be Pisces or Aries.'
        elif birth_month == 'April':
            return 'Your zodiac sign might be Aries or Taurus.'
        elif birth_month == 'May':
            return 'Your zodiac sign might be Taurus or Gemini.'
        elif birth_month == 'June':
            return 'Your zodiac sign might be Gemini or Cancer.'
        elif birth_month == 'July':
            return 'Your zodiac sign might be Cancer or Leo.'
        elif birth_month == 'August':
            return 'Your zodiac sign might be Leo or Virgo.'
        elif birth_month == 'September':
            return 'Your zodiac sign might be Virgo or Libra.'
        elif birth_month == 'October':
            return 'Your zodiac sign might be Libra or Scorpio.'
        elif birth_month == 'November':
            return 'Your zodiac sign might be Scorpio or Sagittarius.'
        elif birth_month == 'December':
            return 'Your zodiac sign might be Sagittarius or Capricorn.'
        else:
            return "I can't determine your zodiac sign, but it's okay. You're the one who will create your own destiny."

    def get_age_difference(self):
        age = self.calculate_age()
        if age < 26:
            x = 26 - age
            return x
        elif age >= 26:
            x = age - 26
            return x

    def get_age_category(self):
        age = self.calculate_age()
        if age < 26:
            return 'younger than me.'
        elif age > 26:
            return 'older than me.'
        elif age == 26:
            return 'the same with me.'

    def print_info(self):
        age = self.calculate_age()
        decades = self.calculate_decades()
        comment_value = self.get_comment()
        age_comparison = self.get_age_difference()
        age_category = self.get_age_category()
        zodiac_sign = self.get_zodiac_sign()

        print(f"\nHi {self.name.strip()}! \nSo you're born on {self.birth_month.strip()} year {self.birth_year}. "
              f"On my calculation you are now {age:,} years old. {comment_value}")

        print(f"You are living in {decades:.1f} decades now "
              f"and you are {age_comparison:,} years {age_category} Amazing!")

        print(zodiac_sign)


# main program
while True:
    name = input('\n\nPlease enter your name: ')
    birth_month = input('Please enter your birth month: ')
    birth_year = int(input('Please enter your birth year: '))

    age_calculator = AgeCalculator(name, birth_month, birth_year)
    age_calculator.print_info()

    response = input("\nDo you want to continue (y/n)? ")
    if response.lower() != "y":
        break
