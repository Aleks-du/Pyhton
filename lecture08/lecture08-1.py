#Написать функцию, которая принимает любой итерируемый объект. Данная функция должна возвращать все отсортированные уникальные элементы в данном итерируемом объекте. 
iterable = input('Введи список через запятую ')
iterable = iterable.split(',')

def Unique(iterable):

    iterable.sort()
    spi = []
    for i in range(len(iterable)):
        if iterable[i] != iterable[i-1]:
            spi.append(iterable[i])
    return spi

print(Unique(iterable))
