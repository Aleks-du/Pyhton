#Написать функцию, которая принимает в себя два аргумента: строку-шаблон и словарь. Строка-шаблон содержит какой-то шаблон для текста, внутри которого есть маркеры, которые нужно заменить некими словами. В словаре маркеры используются в виде ключей. Вам нужно сделать так, чтобы маркеры в шаблоне заменились на значения, которые хранятся в словаре по этим маркерам.

def Template(template, values):

    #template = "Hello, {username}"
    #"{username}".format(username="values")
    key, value = list(values.items())[0]
    #print(value)
    return template.replace("{username}", value)

print(Template(template, {"username": "John"}))
