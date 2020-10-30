#Вариант рабочий, но как он работает я так и не понял.
import random

numbers = [random.randint(0,6) for i in range(10)]
print(numbers)

numbers = list(filter(bool, numbers))

print(numbers)
