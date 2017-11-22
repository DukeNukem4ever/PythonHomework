f = open ("C:\\Users\\Artem\\Desktop\\Homework\\Python\\Lesson4\\Crow.txt", encoding="utf-8")
text = f.read()
lines = text.splitlines()
f.close()
c1 = 0
c2 = 0
for line in text.split("\n"):
    for word in line.split(" "):
        word.replace (',','')
        n = len(word)
        if n > 10:
            c1+=1
        else:
            c2+=1
        print (len(word))
        print(word)
res = c1/(c1+c2) * 100
print("Процент слов, имеющих длину больше десяти слов, =",end = " ")
print (res)


#x = input("Укажите расположение текстового файла: ")
#print(x)
#(C:/Users/Artem/Desktop/Homework/Python/Lesson 4/homework4.py)
#(C:/Users/Artem/Desktop/Homework/Python/Lesson 4/Crow.txt)
#S = "str"
#with open ("C:\\Users\\Artem\\Desktop\\Homework\\Python\\Lesson4\\homework4.py",encoding='utf-8') as f:
#    text = f.read()

#with open ("C:\\Users\\Artem\\Desktop\\Homework\\Python\\Lesson4\\Crow.txt",encoding='utf-8') as f:
#    text = f.read()
#    splited_text = text.split()
#    lines1 = f.readlines()
#    lines2 = text.splitlines()
#    for line in f:    # здесь строки тоже заканчиваются на символ переноса строки
#        if line.endswith("\n"):
#            print("Строка кончается на символ переноса строки")
#        else:
#            print("Строка не заканчивается на символ переноса строки")
#        line = line.strip()    # удаляем пробельные символы, в том числе перенос строки, сначала и сконца строки
#        if not line.endswith("\n"):
#            print("Теперь переноса строки точно нет")
#        if line.startswith("Давным-давно"):    # проверяем не начинается ли строка с данной строки
#            print("И жили они долго и счастливо")
#print (splited_text)
#print (lines1)
#print (lines2)
#print (len(S))

#word_length = len(x)

#f = open ("C:\\Users\\Artem\\Desktop\\Homework\\Python\\Lesson4\\homework4.py",encoding='utf-8') as f:

#text1 = f.read()
