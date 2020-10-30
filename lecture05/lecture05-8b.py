# Не совсем рабочий вариант, надо занулять а не удалять, как и в предыдущем задании.
import random

numbers = [random.randint(0,3) for i in range(10)]
print(numbers)
b=3

for _ in range(len(numbers)):
    for i in range(len(numbers)-1):
        if numbers[i-1] == b:
            del numbers[i-1]
print(numbers)
