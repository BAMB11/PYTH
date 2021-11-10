#дано натуральное число, вычислить простое ли оно или составное

numbers = int(input())
for i in range (2, numbers):
    if numbers % i == 0:
        print ("Число не простое")
        break
    elif numbers // i == 1:
        print ("Число простое")
        break

#вывести все простые числа от 2 до n
    
def simple(numbers):
    for i in range (2, numbers):
        if numbers % i == 0:
            break
        elif numbers // i == 1:
            print (numbers)
            break
        
print('Введите до какого n выводить простые числа')
n = int(input())
for i in range (2, n):
    simple(i)
