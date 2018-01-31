def main():
    ''' '''
    wordlist = []
    length = []
    amount = 0
    dlina = 0
    with open('Pride_and_Prejudice.txt', encoding='utf-8') as f:
        text = f.read()
        text = text.replace('-', '')
        text = text.replace(',', '').replace('.', '')
        words = text.split()
        for word in words:
            if word[-3:] == "ous":
                amount += 1
                wordlist.append(word)
                length.append(len(word))
        print(amount)
        print(round(float(sum(length) / amount)))

if __name__ == '__main__':
    main()
