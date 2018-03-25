import re

def getfamily():
    f = open('wiki.htm','r',encoding='utf-8')
    text = f.read()
    for line in text:
        regex = 'Семейство:</th>\n(.*)?\n(.*)?title="(.*)"'
        res = re.search(regex, line)
    if res:
        print(res.group(3))
        return
    else:
        print('Попробуйте ещё раз')
    f.close()

def main():
    getfamily()

if __name__ == '__main__':
    main()
