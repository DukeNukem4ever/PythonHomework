import re

d = ''
e = ''

with open('wiki.htm', 'r', encoding='utf-8') as sock:
    for line in sock:
        d = d + ' ' + line.replace('\n', '\n')
with open ("output.txt", 'w', encoding = 'utf-8') as f:
    f.write(d)
for line in d:
    match = re.findall(r'Семейство:+\D+\d+\D+\w', d)
    if match:
        reg = re.compile('[^а-яёА-яё ]')
        for line in match:
            e = e + ' ' + line.replace('\n', '\n')
        print(reg.sub('', e))
        with open("log.txt", "w", encoding = "utf-8") as g:
            g.write(reg.sub('', e))
        break
    else:
        print('Попробуйте ещё раз')
        break
sock.close()
