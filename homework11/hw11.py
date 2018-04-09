import re


def main():
    r = open('dino.htm', 'r', encoding = 'utf-8')
    w = open('cat.htm', 'w', encoding = 'utf-8')
    for line in r.readlines():
        repl = re.sub(r'динозавр([а-я](?:[а-я])?)','кот\g<1>',line)
        repl = re.sub(r'динозавр', 'кот', line)
        repl = re.sub(r'Динозавр([а-я](?:[а-я])?)','Кот\g<1>',repl)
        repl = re.sub(r'Динозавр', 'Кот', repl)
        w.write(repl)
    r.close()
    w.close()


if __name__ == '__main__':
    main()
