import random

# Тип сложного предложения

def Type():
    types = ['СПП', 'ССП']
    if random.choice(types) == 'СПП':
        Vid = Pnoun1() + Padv() + Pverb1() + \
              Pnoun2() + Pznak() + Pokt() + Pnoun3() + Pverb2() + Pnoun4()
    else:
        Vid = noun() + adverb() + verb1() + adjective() + noun2() + \
              soiuz() + noun3() + verb2() + obst()
    return Vid

# Сложноподчинённое предложение

def Pnoun1():
    pnouns = ['Кактус', 'Сом', 'Конь', 'Экскурсовод', 'Медведь', 'Охотник', 'Я', 'Мой друг', 'Волк']
    return random.choice(pnouns)
 
def Padv():
    padverbs = ['', ' тихо', ' осторожно', ' весело', ' с беспокойством', ' с удовольствием', ' напряжённо', ' сдержанно']
    return random.choice(padverbs)

def Pnoun2():
    pnouns2 = [' следы', ' слюну', ' улыбку', ' радость', ' слезу', ' злость', ' восторженность', ' эмоцию']
    return random.choice(pnouns2)
 
def Pokt():
    pokts = [' когда', ' несмотря на то, что', ' поскольку', ' вследствие того, что', ' в результате чего', ' так как', ' потому что']
    return random.choice(pokts)

def Pnoun3():
    pnouns3 = [' мой друг', ' Аркадий', ' жеребец', ' охотник', ' браконьер' ,' смотритель', ' хорёк', ' водитель', ' сторож', ' его товарищ']
    return random.choice(pnouns3)

def Pnoun4():
    pnouns4 = [' машину.', ' его.', ' вокруг.', ' зверей.', ' друзей.' ,' реку.', ' автобус.', ' ёлку.', ' меня.']
    return random.choice(pnouns4)
 
def Pznak():
    pznaks = [',']
    return random.choice(pznaks)

def Pverb1():
    pverbs1 = [' обронил', ' сглотнул', ' показал на', ' проглотил', ' скрыл свою']
    return random.choice(pverbs1)

def Pverb2():
    pverbs2 = [' упустил', ' увидел', ' ограбил', ' опередил', ' победил', ' осмотрел', ' завёл', ' оставил', ' пощадил', ' разобрал', ' успел поймать', ' догнал', ' услышал']
    return random.choice(pverbs2)

# Сложносочинённое предложение

def noun():
    nouns = ['Заяц', 'Барсук', 'Охотник', 'Грибник', 'Медведь', 'Змей', 'Лесоруб', 'Водитель', 'Бегемот']
    return random.choice(nouns)
 
def adverb():
    adverbs = ['', ' с оглядкой', ' медленно', ' весело', ' осторожно', ' с удовольствием', ' со слезами на глазах']
    return random.choice(adverbs)

def noun2():
    nouns2 = [' машину', ' белку', ' хижину', ' ёлку', ' реку' ,' девочку', ' деревню', ' сосну', ' крышу']
    return random.choice(nouns2)
 
def adjective():
    adjectives = [' маленькую', ' чёрную', ' большую', ' красную', ' непослушную', ' новую', ' грязную', ' просторную', ' свою']
    return random.choice(adjectives)
 
def soiuz():
    soiuzes = [';', ', и', ', и так', ', а', ', а затем', ', и тут']
    return random.choice(soiuzes)

def noun3():
    nouns3 = [' он', ' волк', ' олень', ' лис', ' его друг', ' отец девочки', ' я', ' ястреб', ' наш учитель']
    return random.choice(nouns3)

def verb1():
    verbs = [' срубил', ' залез на', ' открыл', ' осмотрел', ' завёл', ' оставил', ' разрушил', ' подобрал', ' схватил', ' разбил', ' навестил']
    return random.choice(verbs)

def obst():
    obsts = [' на него.', ' прочь.', ' домой.', ' там.', ' громко.', ' с улыбкой на лице.']
    return random.choice(obsts)
 
def verb2():
    verbs2 = [' набросился', ' уехал', ' заплакал', ' разозлился', ' спустился', ' заночевал', ' убежал', ' рассмеялся']
    return random.choice(verbs2)

def main():
    amount = ['5', '6', '7', '8', '9', '10']
    if random.choice(amount) == '5':
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
    elif random.choice(amount) == '6':
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
    elif random.choice(amount) == '7':
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
    elif random.choice(amount) == '8':
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
    elif random.choice(amount) == '9':
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
    else:
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())
        print()
        print(Type())

if __name__ == '__main__':
    main()
