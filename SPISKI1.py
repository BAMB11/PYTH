S = [2,3,1,6,8,4,9,0,6,4,7,8,0,4,5,2,4]

def maximum(S):
    maxnum = S[0]
    for x in S:
        if x > maxnum:
            maxnum = x
    return maxnum
    
def summ(S):
    summa = 0
    for x in S:
        summa += x
    return summa

def avg(S):
    summa = summ(S)
    return summa / len(S)

def median(S):
    center = 0
    S.sort()
    if len(S) % 2 == 0:
        center = len(S) / 2
        return center
    else:
        return avg(S)

def nullcounter(S):
    null=0
    for x in S:
        if x == 0:
            null+=1
    return null
    
print('Сумма элементов списка = ', summ(S))
print('Максимальный элемент списка = ', maximum(S))
print('Среднее арифметическое значение = ', avg(S))
print('Медиана = ', median(S))
print('Количество нулей = ', nullcounter(S))
