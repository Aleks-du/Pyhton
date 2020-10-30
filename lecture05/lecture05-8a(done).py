#8
# Дан список X, состоящий из целых чисел и целое число b. Исключить из списка элементы, равные b. b=3
import random

numbers = [random.randint(0,3) for i in range(10)]
print(numbers)
b=3
while b in numbers: #для всех b в списке
    numbers.remove(b) #удаляем его из списка
print(numbers)
