#ct = ""
count = 0
with open ("F.xml", "r", encoding="utf-8") as f:
    for line in f.readlines():
        count += 1
    ct = (' '.join([str(count)]))
with open ("Kolvo.txt", "w", encoding="utf-8") as f:
    f.write(ct)
