import re

d = ''
with open('Text.txt', 'r', encoding='utf-8') as f:
    for line in f:
        d = d + ' ' + line.replace('\n', ' ')

#d = set(open('Text.txt', 'r', encoding='utf-8'))

result1 = re.search(r'съесть', d)

result2 = re.search(r'Съесть', d)

result3 = re.search(r'съем', d)

result4 = re.search(r'Съем', d)


result5 = re.search(r'съел', d)

result6 = re.search(r'Съел', d)

    
result7 = re.search(r'съела', d)

    
result8 = re.search(r'Съела', d)

    
result9 = re.search(r'съело', d)


result10 = re.search(r'Съело', d)


    
result11 = re.search(r'съели', d)

    
result12 = re.search(r'Съели', d)

    
result13 = re.search(r'съеден', d)

result14 = re.search(r'Съеден', d)


    
result15 = re.search(r'съеденный', d)

    
result16 = re.search(r'Съеденный', d)

    
result17 = re.search(r'съестное', d)

result18 = re.search(r'Съестное', d)

result19 = re.search(r'съедобный', d)

result20 = re.search(r'Съедобный', d)    
result21 = re.search(r'съешь', d)
result22 = re.search(r'Съешь', d)
result23 = re.search(r'сьедим', d)
result24 = re.search(r'Cъедим', d)
result25 = re.search(r'съедите', d)
result26 = re.search(r'Съедите', d)
result27 = re.search(r'съедят', d)
result28 = re.search(r'Съедят', d)
result29 = re.search(r'съевший', d)    
result30 = re.search(r'Съевший', d)
result31 = re.search(r'съев', d)
result32 = re.search(r'Съев', d)
result33 = re.search(r'съевши', d)
result34 = re.search(r'Съевши', d)
result35 = re.search(r'съест', d)
result36 = re.search(r'Съест', d)
result37 = re.search(r'съешьте', d)
result38 = re.search(r'Съешьте', d)
result39 = re.search(r'несъеденный', d)
result40 = re.search(r'Несъеденный', d)
result41 = re.search(r'съеденная', d)
result42 = re.search(r'Съеденная', d)
result43 = re.search(r'съеденное', d)
result44 = re.search(r'Съеденнон', d)
result45 = re.search(r'съеденные', d)
result46 = re.search(r'Съеденные', d)
result47 = re.search(r'несъеденная', d)
result48 = re.search(r'Несъеденная', d)
result49 = re.search(r'несъеденное', d)
result50 = re.search(r'Несъеденное', d)
result51 = re.search(r'несъеденные', d)
result52 = re.search(r'Несъеденные', d)
result53 = re.search(r'съевшая', d)
result54 = re.search(r'Съевшая', d)
result55 = re.search(r'съевшее', d)
result56 = re.search(r'Съевшее', d)
result57 = re.search(r'съевшие', d)
result58 = re.search(r'Съевшие', d)
result59 = re.search(r'съевшим', d)
result60 = re.search(r'Съевшим', d)
result61 = re.search(r'съевшей', d)
result62 = re.search(r'Съевшей', d)
result63 = re.search(r'съевшой', d)
result64 = re.search(r'Съевшой', d)
result65 = re.search(r'съевшими', d)
result66 = re.search(r'Съевшими', d)
result67 = re.search(r'съевшему', d)
result68 = re.search(r'Съевшему', d)
result69 = re.search(r'съевших', d)
result70 = re.search(r'Съевших', d)
result71 = re.search(r'съевшими', d)
result72 = re.search(r'Съевшими', d)
result73 = re.search(r'съевшего', d)
result74 = re.search(r'Съевшего', d)
result75 = re.search(r'съевшею', d)
result76 = re.search(r'Съевшею', d)
result77 = re.search(r'съедим', d)
result78 = re.search(r'Съедим', d)
result79 = re.search(r'съеденного', d)
result80 = re.search(r'Съеденного', d)
result81 = re.search(r'съеденной', d)
result82 = re.search(r'Съеденной', d)
result83 = re.search(r'съеденных', d)
result84 = re.search(r'Съеденных', d)
result85 = re.search(r'съеденному', d)
result86 = re.search(r'Съеденному', d)
result87 = re.search(r'съеденным', d)
result88 = re.search(r'Съеденным', d)
result89 = re.search(r'съеденную', d)
result90 = re.search(r'Съеденную', d)
result91 = re.search(r'съеденною', d)
result92 = re.search(r'Съеденною', d)
result93 = re.search(r'съеденными', d)
result94 = re.search(r'Съеденными', d)
result95 = re.search(r'съеденном', d)
result96 = re.search(r'Съеденном', d)
result97 = re.search(r'съедено', d)
result98 = re.search(r'Съедено', d)
result99 = re.search(r'съедена', d)
result100 = re.search(r'Съедена', d)
result101 = re.search(r'съедены', d)
result102 = re.search(r'Съедены', d)
result103 = re.search(r'несъеденного', d)
result104 = re.search(r'Несъеденного', d)
result105 = re.search(r'несъеденной', d)
result106 = re.search(r'Несъеденной', d)
result107 = re.search(r'несъеденных', d)
result108 = re.search(r'Несъеденных', d)
result109 = re.search(r'несъеденному', d)
result110 = re.search(r'Несъеденному', d)
result111 = re.search(r'несъеденным', d)
result112 = re.search(r'Несъеденным', d)
result113 = re.search(r'несъеденную', d)
result114 = re.search(r'Несъеденную', d)
result115 = re.search(r'несъеденною', d)
result116 = re.search(r'Несъеденною', d)
result117 = re.search(r'несъеденными', d)
result118 = re.search(r'Несъеденными', d)
result119 = re.search(r'несъеденном', d)
result120 = re.search(r'Несъеденном', d)

if result1 is None:
    print("None")

if result2 is None:
    print("None")

if result3 is None:
    print("None")

if result4 is None:
    print("None")

if result5 is None:
    print("None")

if result6 is None:
    print("None")

if result7 is None:
    print("None")

if result8 is None:
    print("None")

if result9 is None:
    print("None")

if result10 is None:
    print("None")

if result11 is None:
    print("None")

if result12 is None:
    print("None")

if result13 is None:
    print("None")

if result14 is None:
    print("None")

if result15 is None:
    print("None")

if result16 is None:
    print("None")

if result17 is None:
    print("None")

if result18 is None:
    print("None")

if result19 is None:
    print("None")

if result20 is None:
    print("None")

if result21 is None:
    print("None")

if result22 is None:
    print("None")

if result23 is None:
    print("None")

if result24 is None:
    print("None")

if result25 is None:
    print("None")

if result26 is None:
    print("None")

if result27 is None:
    print("None")

if result28 is None:
    print("None")

if result29 is None:
    print("None")

if result30 is None:
    print("None")

if result31 is None:
    print("None")

if result32 is None:
    print("None")

if result33 is None:
    print("None")

if result34 is None:
    print("None")

if result35 is None:
    print("None")

if result36 is None:
    print("None")

if result37 is None:
    print("None")

if result38 is None:
    print("None")

if result39 is None:
    print("None")

if result40 is None:
    print("None")

if result41 is None:
    print("None")

if result42 is None:
    print("None")

if result43 is None:
    print("None")

if result44 is None:
    print("None")

if result45 is None:
    print("None")

if result46 is None:
    print("None")

if result47 is None:
    print("None")

if result48 is None:
    print("None")

if result49 is None:
    print("None")

if result50 is None:
    print("None")

if result51 is None:
    print("None")

if result52 is None:
    print("None")

if result53 is None:
    print("None")

if result54 is None:
    print("None")

if result55 is None:
    print("None")

if result56 is None:
    print("None")

if result57 is None:
    print("None")

if result58 is None:
    print("None")

if result59 is None:
    print("None")

if result60 is None:
    print("None")

if result61 is None:
    print("None")

if result62 is None:
    print("None")

if result63 is None:
    print("None")

if result64 is None:
    print("None")

if result65 is None:
    print("None")

if result66 is None:
    print("None")

if result67 is None:
    print("None")

if result68 is None:
    print("None")

if result69 is None:
    print("None")

if result70 is None:
    print("None")

if result71 is None:
    print("None")

if result72 is None:
    print("None")

if result73 is None:
    print("None")

if result74 is None:
    print("None")

if result75 is None:
    print("None")

if result76 is None:
    print("None")

if result77 is None:
    print("None")

if result78 is None:
    print("None")

if result79 is None:
    print("None")

if result80 is None:
    print("None")

if result81 is None:
    print("None")

if result82 is None:
    print("None")

if result83 is None:
    print("None")

if result84 is None:
    print("None")

if result85 is None:
    print("None")

if result86 is None:
    print("None")

if result87 is None:
    print("None")

if result88 is None:
    print("None")

if result89 is None:
    print("None")

if result90 is None:
    print("None")

if result91 is None:
    print("None")

if result92 is None:
    print("None")

if result93 is None:
    print("None")

if result94 is None:
    print("None")

if result95 is None:
    print("None")

if result96 is None:
    print("None")

if result97 is None:
    print("None")

if result98 is None:
    print("None")

if result99 is None:
    print("None")

if result100 is None:
    print("None")

if result101 is None:
    print("None")

if result102 is None:
    print("None")

if result103 is None:
    print("None")

if result104 is None:
    print("None")

if result105 is None:
    print("None")

if result106 is None:
    print("None")

if result107 is None:
    print("None")

if result108 is None:
    print("None")

if result109 is None:
    print("None")

if result110 is None:
    print("None")

if result111 is None:
    print("None")

if result112 is None:
    print("None")

if result113 is None:
    print("None")

if result114 is None:
    print("None")

if result115 is None:
    print("None")

if result116 is None:
    print("None")

if result117 is None:
    print("None")

if result118 is None:
    print("None")

if result119 is None:
    print("None")

if result120 is None:
    print("None")

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)
print(result9)
print(result10)
print(result11)
print(result12)
print(result13)
print(result14)
print(result15)
print(result16)
print(result17)
print(result18)
print(result19)
print(result20)
print(result21)
print(result22)
print(result23)
print(result24)
print(result25)
print(result26)
print(result27)
print(result28)
print(result29)
print(result30)
print(result31)
print(result32)
print(result33)
print(result34)
print(result35)
print(result36)
print(result37)
print(result38)
print(result39)
print(result40)
print(result41)
print(result42)
print(result43)
print(result44)
print(result45)
print(result46)
print(result47)
print(result48)
print(result49)
print(result50)
print(result51)
print(result52)
print(result53)
print(result54)
print(result55)
print(result56)
print(result57)
print(result58)
print(result59)
print(result60)
print(result61)
print(result62)
print(result63)
print(result64)
print(result65)
print(result66)
print(result67)
print(result68)
print(result69)
print(result70)
print(result71)
print(result72)
print(result73)
print(result74)
print(result75)
print(result76)
print(result77)
print(result78)
print(result79)
print(result80)
print(result81)
print(result82)
print(result83)
print(result84)
print(result85)
print(result86)
print(result87)
print(result88)
print(result89)
print(result90)
print(result91)
print(result92)
print(result93)
print(result94)
print(result95)
print(result96)
print(result97)
print(result98)
print(result99)
print(result100)
print(result101)
print(result102)
print(result103)
print(result104)
print(result105)
print(result106)
print(result107)
print(result108)
print(result109)
print(result110)
print(result111)
print(result112)
print(result113)
print(result114)
print(result115)
print(result116)
print(result117)
print(result118)
print(result119)
print(result120)

#print("СЛОВА, НАЧИНАЮЩИЕСЯ СО СТРОЧНОЙ БУКВЫ:")
#print()
#for word in result1:
#    if word[:4] == 'съез' or word[:4] != 'съеб' or word[:4] != 'съеж' or word[:4] != 'съех': # на случай, если в тексте будут матерные слова
#        print(word)
#print()
#print("СЛОВА, НАЧИНАЮЩИЕСЯ С ЗАГЛАВНОЙ БУКВЫ:")
#print()
#for word in result2:
#    if word[:4] != 'Съез' or word[:4] != 'Съеб' or word[:4] != 'Съеж' or word[:4] != 'Съех': # на случай, если в тексте будут матерные слова
#        print(word)
#        if word == word:
#            del(word)
#print()
#print("СЛОВА С ПРИСТАВКОЙ, НАЧИНАЮЩИЕСЯ СО СТРОЧНОЙ БУКВЫ:")
#print()
#for word in result3:
#    if word[:4] != 'несъез' or word[:4] != 'несъеб' or word[:4] != 'несъеж' or word[:4] != 'несъех': # на случай, если в тексте будут матерные слова
#        if word[0] != word[1]:
#            print(word)
#print()
#print("СЛОВА С ПРИСТАВКОЙ, НАЧИНАЮЩИЕСЯ С ЗАГЛАВНОЙ БУКВЫ:")
#print()
#for word in result4:
#    if word[:4] != 'Несъез' or word[:4] != 'Несъеб' or word[:4] != 'Несъеж' or word[:4] != 'Несъех': # на случай, если в тексте будут матерные слова
#        print(word)


