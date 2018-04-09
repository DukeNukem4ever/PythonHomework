import re
import string
#freq = {}
with open('F.xml', 'r', encoding='utf-8') as f:
    string = f.read().lower()
    pattern = re.findall(r'f+\w+', string)
    for word in pattern:
        if word[2] == "h":
            print(word)
        else:
            print("Такого слова нет")
