x = input("Введите слово: ")
print(x)
word_length = len(x)
result1 = x[0:int(word_length/2)]
result2 = x[int(word_length/2):int(word_length)+1]
if word_length % 2 == 1:
    print ("Даное слово имеет нечётное количество букв")
    print (result1);
    print (result2 [::-1])
elif word_length % 2 == 0:
    print ("Даное слово имеет чётное количество букв")
    print (result1);
    print (result2 [::-1])
else:
    print ("Невозможно вычислить")
print ("Всё.")
