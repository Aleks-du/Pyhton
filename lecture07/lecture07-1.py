def Parabola(x):
    return x**2

def Line(x):
    return 2*x

def Extremum(a, b, *, func, **kargs):
    for x in range(a, b + 1):
        if func(x) == func(-x):
            if a <= 0 <= b:
                return 'равен 0'
            return 'отсутствует'
        return 'отсутствует'

result = Extremum(-2, 2, func=Parabola)
print(result) # должно быть 0

result = Extremum(-20, -10, func=Parabola)
print(result) # должно быть None

result = Extremum(-20, 20, func=Line)
print(result) # должно быть None
