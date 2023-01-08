"""
age_calculator.py

    Capabilities:
        Differentiate user's age from the program's author.
            It will tell the user if they are older or younger than the author.
        Calculate the age of famous personalities in history as if they are still living today.
        The program will give an additional comment base on the age range of the user.
        It will convert user's age to decade.


    Limitations:
        The program will keep on looping until the user terminate it via IDE or make it crash.
        If the user lives in the time of BC/BCE, the year must be negative. If not it will return an AD calculation.
            Example: 600 BCE => -600
        Can't determine the exact zodiac sign of the user because there's no input for day

    Improvements:
        Create while loop with exit condition
            - don't know how to incorporate this
        Compare the user's age
        [done] Add Zodiac Sign Identification
            Your zodiac sign might be Aries or Pisces.
            I can't determine your zodiac sign, but it's okay. You're the one who will create your own destiny.
        Debug zodiac_sign function

"""


# Condition for every stage of life
def my_comment():
    if age < -1:
        return 'You are not yet born in this world.'
    elif age < 1:
        return 'You must still be inside your mom\'s womb.'
    elif age < 10:
        return 'So you\'re still in elementary, enjoy your childhood and keep playing!'
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


# Condition for zodiac signs
def my_zodiac():
    if birth_month == 'January':
        return 'Your zodiac sign might be Capricorn or Aquarius.'
    elif birth_month == 'February':
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


# Calculate difference between my age and other people
def age_range():
    if age < 26:
        x = 26 - age
        return x
    elif age >= 26:
        x = age - 26
        return x


# Check if they are younger, older, or the same age
def age_level():
    if age < 26:
        return 'younger than me.'
    elif age > 26:
        return 'older than me.'
    elif age == 26:
        return 'the same with me.'


# This line is used so that the line of While will be read by interpreter and moves to the next line.

# Define variables
while True:
    name = input('\n\nPlease enter your name: ')
    birth_month = input('Please enter your birth month: ')
    birth_year = int(input('Please enter your birth year: '))

    # The current year is 2022
    age = 2022 - birth_year
    decades = float(age / 10)
    comment_value = my_comment()
    age_comparison = age_range()
    age_category = age_level()
    zodiac_sign = my_zodiac()

    print(f"\nHi {name.strip()}! \nSo you're born on {birth_month.strip()} year {birth_year}. "
          f"On my calculation you are now {age:,} years old. {comment_value}")

    print(f"You are living in {decades} decades now "
          f"and you are {age_comparison:,} years {age_category} Amazing!")

    print(zodiac_sign)