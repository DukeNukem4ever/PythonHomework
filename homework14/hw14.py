from collections import Counter
import string

def main():
    ''' '''
    file = ''.join(open('file.txt', 'r', encoding='utf-8-sig')).rstrip(
        string.punctuation)
    words = file.lower().split()
    out_sentence = ""
    for word in words:
        for letter in word:
            for _ in range(word.count(letter)):
                out_sentence += letter
        out_sentence += " "
    print(out_sentence)

if __name__ == '__main__':
    main()
