import os
amount = 0
start_path = 'bbc'
fnames = os.listdir(start_path)
for fname in fnames:
    if '.' not in fname:
        if ' ' in fname:
            amount += 1
            print(fname)
print("Количество требуемых Вами папок:", amount)
