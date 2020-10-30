#6
# Дан список любых целых чисел. Исключить из него
# A.максимальный элемент 
# B.минимальный элемент.
import random

# создаем список случаных элементов от 0 до 20 из 10 элементов
numbers = [random.randint(0, 20) for _ in range(10)]
print(numbers)

cop = numbers.copy() #делаем копию списка

numbers.remove(max(numbers)) #исключаем максимальный элемент
print('A=', numbers)

cop.remove(min(cop)) #исключаем минимальный элемент
print('B=', cop)
