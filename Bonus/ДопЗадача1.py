# list = []
# amount = 0
# while True:
#    number = input("Введите число \n")
#    print(number.upper())
#    if number == "":
#        break
#    else:
#        list.append(number)
#        amount +=1
# print("Результат:")
# print("Количество введённых цифр: " + amount)
# print(list)

# with open("Text.txt", "w") as f:
#    def listsum(numList):
#        if len(numList) == 1:
#            return numList[0]
#        else:
#            return numList[0] + listsum(numList[1:])
#    print(listsum(number)//amount)
# list = []
# summa = 0
# kolichestvo = 0
# while True:
#    x = int(input("Введите число \n"))
#    print (x)
#    if x == "":
#        break
#    else:
#        list.append(x)
#        kolichestvo +=1
# print("End.")
# print(list)


# with open("Text.txt", "w") as f:
#    while x != 0:
#        summa += x
#        kolichestvo += 1
#        x = int(input())
#        srednee = summa/kolichestvo
#        print('Среднее значение:', srednee)

# -*- coding: utf-8 -*-

sum, n, num = 0, 0, 0
list = []
while True:
    print("Введите число")
    num = input()
    if num == "":
        break
    num = int(num)
    sum += num
    n += 1
    list.append(num)
print("Среднее арифметическое число равно ", sum / n)
print(min(list))
print(max(list))
