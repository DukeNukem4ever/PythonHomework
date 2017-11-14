x = input("Введите слово: ")
print(x)
word_length = len(x)
letters = []
for j in reversed (x):
    letters.append (j)
    print (letters[::-1])
    
