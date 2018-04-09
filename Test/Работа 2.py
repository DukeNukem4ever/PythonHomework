import re
import string
freq = {}
with open('F.xml', 'r', encoding='utf-8') as f:
    string = f.read().lower()
    pattern = re.findall(r'<w lemma=+\W+\w+\W+', string)
    for word in pattern:
        count = freq.get(word,0)
        freq[word] = count + 1
    freq_list = freq.keys()

with open('Res.txt', 'w', encoding = 'utf-8') as f:
    for words in freq_list:
        result = ''.join([str(words)])#.join([str(freq[words])]))
        res = result.replace("<w lemma=","")
        result2 = ''.join([str(freq[word])])
        f.write(res)
        f.write(result2)
        f.write("\n")
