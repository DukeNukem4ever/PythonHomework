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
