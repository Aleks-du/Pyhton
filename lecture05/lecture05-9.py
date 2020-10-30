#9
# Дан список целых чисел X и числа A1, A2 и A3. Включить эти числа в список, расположив их после второго элемента.
import random

numbers = [random.randint(0,15) for i in range(10)]
print(numbers)
print('Ввести три числа, которые встанут в список после второго элемента')
A1 = int(input('A1 = ', ))
A2 = int(input('A2 = ', ))
A3 = int(input('A3 = ', ))

numbers.insert(2, A1)
numbers.insert(3, A2)
numbers.insert(4, A3)
print(numbers)
