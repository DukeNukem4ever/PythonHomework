import os

amount = 0

start_path = '.'
for root, dirs, files in os.walk(start_path):
    print('Где мы сейчас:', root)
    print('Количество файлов:')
    for file in files:
        print(file)
        amount += 1
print(amount)
