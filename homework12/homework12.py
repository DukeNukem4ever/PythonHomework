import os
amount = 0
fnames = os.listdir()
for fname in fnames:
    if '.' not in fname:
        if ' ' or '_' or ',' or ';' or ':' in fname:
            amount += 1
            print(fname)
print()
print("Количество требуемых Вами папок:", amount)
