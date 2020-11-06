s = input('2 слова через пробел: ',)
sl = s.split()
if len(sl) !=2: #len - список (для списка равно двум
    exit(1)

word1=sl[0].lower() #в нижний регистр
word2=sl[1].lower()

result = [] #где будем хранить значение

for char1 in word1: #для каждого символа из первого слова
    for char2 in word2: #для каждого слова из второго слова
        if char1 == char2: 
            if char1 not in result:
                result.append(char1) 
		
for char in sorted(result): # сортируем
    print(char)
