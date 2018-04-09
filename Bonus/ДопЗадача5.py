x = input("Введите слово: ")
print(x)
new_word = ''
CONSTANTS = 'qwrtpsdfghjklzxcvbnmQWRTPSDFGHJKLZXCVBNM'
for letter in x:
    if letter.lower() in CONSTANTS:
        new_word += letter
        'aig'.join (letter)
    else:
        new_word += letter 
print (*new_word, sep ='aig')
