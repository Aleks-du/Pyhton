#Не совсем рабочий вариант, надо занулять а не удалять, но до двух нулей работает.
import random

numbers = [random.randint(0,6) for i in range(10)]
print(numbers)

for _ in range(len(numbers)): # проходим по всем доступным индексам в списке
    for i in range(len(numbers)-1): #В списке всегда -1 потому что начинаем с нуля
         if numbers[i-1] == 0: #если элемент равен 0
            del numbers[i-1] #удаляяем его

print(numbers)
