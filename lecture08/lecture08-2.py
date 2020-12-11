#Написать функцию, которая принимает некоторую строку и проверяет, является ли данная строка палиндромом.
s = input("Введите слово: ")

def Palindrome(s):
    s = s.lower() #если введет А или а, буква одна и та же
    if len(s) == 1 or len(s) == 0: 
        return True 
    if s[0] == s[-1]:  
        return Palindrome(s[1:-1]) #срезаем 1 и -1 символы и прогоняем ещё раз пока есть что
    else:
        return False 
print(Palindrome(s))
