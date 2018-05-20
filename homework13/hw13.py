import os

def program():
    amount = 0
    prev1 = None
    prev2 = None
    start_path = '.'
    for root, dirs, files in os.walk(start_path):
        print('Где мы сейчас:', root)
        print('Количество файлов:')
        for dire in dirs:
            if dire != prev1:
                print(dire)
                amount += 1
            prev1 = dire
        for file in files:
            if file != prev2:
                print(file)
                amount += 1
            prev2 = file
    print(amount)
    return amount

program()
