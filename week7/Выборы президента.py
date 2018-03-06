finput = open('input.txt', 'r', encoding='utf-8')
foutput = open('output.txt', 'w', encoding='utf-8')

voices = {}
voiceCount = 0
result = []

for i in finput:
    key = i.strip()
    voiceCount += 1
    voices[key] = voices.get(key, 0) + 1

for key in voices:
    result.append((voices[key], key))

result.sort(reverse=True)

print(result[0][1], file=foutput)

if result[0][0] <= voiceCount / 2:
    print(result[1][1], file=foutput)
foutput.close()
