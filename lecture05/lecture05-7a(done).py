#7
# Дан список из любых целых чисел, в котором есть два нулевых элемента. Исключить нулевые элементы.
import random

numbers = [random.randint(0,6) for i in range(10)]
print(numbers)

while 0 in numbers: #удаляем до тех пор 0
    numbers.remove(0)

print(numbers)
