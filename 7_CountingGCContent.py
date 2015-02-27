f = []
f = open('cons.txt', 'r').read().split('>')

names = []
strings = []
GCstrings = []
for i in range(0, len(f)):
    row = f[i].splitlines() #каждую строку делим на подстроки
    s = ""
    if row:
        _name = row[0]
        names.append(_name)
    for j in range(1,len(row)): #склеиваем все кроме имени в одну длинную
        _tmp = row[j]
        s += _tmp
    strings.append(s)
#print(strings)

for i in range(0, len(strings)):
    _t = str(strings[i])
    if _t:
        value = (_t.count('G') + _t.count('C')) / len(_t)
        value = value * 100
        value = round(value, 6)
        GCstrings.append(value)

for q in range(0, len(GCstrings)):
    print(names[q])
    print(GCstrings[q])

print("--------------")
print(max(GCstrings))