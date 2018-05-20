import os

def stat(prev1,prev2, amount, start_path):
    for root, dirs, files in os.walk(start_path):
        print()
        print('ГДЕ МЫ СЕЙЧАС:', root)
        print()
        print('ФАЙЛЫ:')
        print()
        for dire in dirs:
            print(dire)
            if dire != prev1:
                amount += 1
            prev1 = dire
        for file in files:
            print(file)
            if file != prev2:
                amount += 1
            prev2 = file
    print(amount)
    return amount

stat(None, None, 0, '.')
