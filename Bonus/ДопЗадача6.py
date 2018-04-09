height = int(input("Введите рост своего тела: "))
weight = int(input("Введите вес своего тела: "))
height2 = height / 100
index = weight / (height2 ** 2)
print("Индекс массы тела: ", index)
while True:
    if index <= 16:
        print("Выраженный дефицит массы тела")
        break
    elif 16 < index < 18.5:
        print("Недостаточная масса тела")
        break
    elif 18.5 < index < 24.99:
        print("Норма")
        break
    elif 25 < index < 30:
        print("Избыточная масса тела")
        break
    elif 30 < index < 35:
        print("Ожирение первой степени")
        break
    elif 35 < index < 40:
        print("Ожирение второй степени")
        break
    elif index >= 40:
        print("Ожирение третей степени")
        break
