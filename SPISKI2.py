#Найти самое длинное слово из списка
spisok = ['метод','файл','автомобиль','наушники','макароны']
s = 0
for word in spisok:
    if len(word) > s:
        res = word
        s = len(word)
print('Самое длинное слово: ',res)

#Список слов, короче 5 букв
lists=[]
for word in spisok:
    if len(word) < 5:
        lists.append(word)
print('Cлова короче 5 букв: ',lists)

#Разделить на 2 списка: список слов,начинающихся на гласную и на согласную
glas=[]
neglas=[]
for word in spisok:
    if word[0] in ['а','о','у','э','ы','я','ё','е','ю','и']:
        glas.append(word)
    else:
        neglas.append(word)
print('Список слов, начинающихся с согласной: ',glas)
print('Список слов, начинающихся с негласной: ',neglas)

resword = 1
spisok.sort()
curword = spisok[0]
for word in spisok:
    if curword != word:
        curword = word
        resword += 1
print('Уникальных слов в списке: ', resword)
