list = []
while True:
    word = input ("Введите слово \n")
    print (word.upper())
    if word == "":
        break
    else:
        list.append (word)
print ("End.")
print (list)

with open ("Text.txt", "w") as f:
    for word in list:
        if word [-3:] == "tur":
            f.write(word + "\n")
