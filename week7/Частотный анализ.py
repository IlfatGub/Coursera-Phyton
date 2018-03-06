d = {}
in_file = open("input.txt", "r", encoding="utf8")
for i in range(20):
    for word in in_file.read().split():
        d[word] = d.get(word, 0) + 1

for i in sorted(d.items(), key=lambda x: (-x[1], x[0])):
    print(i[0])
