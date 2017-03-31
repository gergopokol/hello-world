import string

sentence = 'Jim quickly realized that the beautiful gowns are expensive'

def counter(input_string):
    alphabet = string.ascii_letters
    count_letters = {}
    for character in alphabet:
        if sentence.count(character) > 0:
            count_letters[character] = sentence.count(character)
    return(count_letters)

address_count=counter(sentence)

most_letters_count=1
for letter in address_count.keys():
    if address_count[letter] > most_letters_count:
        most_letters_count = address_count[letter]
        most_frequent_letter = letter

print(most_frequent_letter)