from textblob import TextBlob


def convert(string):
    list_var = list(string.split())
    return list_var

string_var = input('\nEnter your word: ')
words = convert(string_var)
corrected_words = []

for word in words:
    corrected_words.append(TextBlob(word))

print(f'\nWords to check: {words}')

print('\nCorrected words are:\n')
for corrected_word in corrected_words:
    print(f'\t- {corrected_word.correct()}')

