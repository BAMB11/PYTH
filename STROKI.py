a = 'leg right monitor far'
b = a.split()
print(len(b))

#(hello -> h*ll*)

a = 'right monitor'
for x in a:
    if x in "АаЕеIiOoUuYy":
        a = a.replace(x,'*')
        
print(a)

#выбросить из нее все слова короче 4 букв

a = 'hello my teacher hello my friends'
b = a.split()
c = []

for a in b:
    if len(a)>4:
        c.append(a)
print(c)
