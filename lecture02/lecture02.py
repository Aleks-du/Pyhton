stroka = input("Введите число от 0 до 99 : ")
stroka = stroka.strip() # удаляем пробелы


if not (1 <= len(stroka) <= 2): #проверяем чтобы длина строки было 1 или 2 символа
    print("Слишком много символов")
    exit(1)
    
if not stroka.isdigit(): #проверяме, чтобы были только числа
    print("Не соответствует заданным параметрам")
    exit(1)

    
numb = int(stroka) #преобраззуем строку в число


if not(0 <= numb <= 99): #проверяем, что входит в наш диапазон
    print("не входит в наш диапазон")
    exit(1)

otvet = ""

if numb // 10 == 2:
    otvet += "двадцать "
elif numb // 10 == 3:
    otvet += "тридцать "
elif numb // 10 == 4:
    otvet += "сорок "
elif numb // 10 == 5:
    otvet += "пятьдесят "
elif numb // 10 == 6:
    otvet += "шестьдесят "
elif numb // 10 == 7:
    otvet += "семдесят "
elif numb // 10 == 8:
    otvet += "восемьдесят "
elif numb // 10 == 9:
    otvet += "девяносто "

    
if numb == 0 and numb:
    otvet = otvet + "нуль"
elif numb % 10 == 1:
    otvet += "один"
elif numb % 10 == 2:
    otvet += "два"
elif numb % 10 == 3:
    otvet += "три"
elif numb % 10 == 4:
    otvet += "четыре"
elif numb % 10 == 5:
    otvet += "пять"
elif numb % 10 == 6:
    otvet += "шесть"
elif numb % 10 == 7:
    otvet += "семь"
elif numb % 10 == 8:
    otvet += "восемь"
elif numb % 10 == 9:
    otvet += "девять"
    
elif numb == 10:
    otvet += "десять"    
elif numb == 11:
    otvet += "одинннадцать"
elif numb == 12:
    otvet += "двенадцать"
elif numb == 13:
    otvet += "тринадцать"
elif numb == 14:
    otvet += "четырнадцать"
elif numb == 15:
    otvet += "пятнадцать"
elif numb == 16:
    otvet += "шестнадцать"
elif numb == 17:
    otvet += "семнадцать"
elif numb == 18:
    otvet += "восемнадцать"
elif numb == 19:
    otvet += "девятнадцать"

print(f"Ответ: {otvet}")
