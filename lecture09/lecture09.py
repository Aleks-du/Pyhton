#1
#Создать класс транспортного средства Vehicle с атрибутами экземпляра класса:
#max_speed (максимальная скорость), mileage (пробег), capacity (количество посадочных мест), name (название средства).
#Добавьте методы, которые смогут изменять и получать эти атрибуты: set_max_speed, get_max_speed, set_capacity и так далее.

#self - это ссылка на текущий экземпляр класса
class Vehicle:
    # это атрибут класса
    
    def __init__(self, max_speed, mileage, capacity, name): 
        # А вот это создаст атрибут экземпляра во время его создания
        self.max_speed = max_speed #скорость
        self.mileage = mileage #пробег
        self.capacity = capacity #посдаочные места
        self.name = name #название
    
    # это метод класса
    def set_max_speed(self):
        self.max_speed = max_speed
    def get_max_speed(self):
        return self.max_speed
    
    def set_mileage(self):
        self.mileage = mileage
    def get_mileage(self):
        return self.mileage
    
    def set_capacity(self):
        self.capacity = capacity
    def get_capacity(self):
        return self.capacity
    
    def set_name(self):
        self.name = name
    def get_name(self):
        return self.name

#2
#Создать класс автобуса Bus, который наследует все атрибуты и методы класса Vehicle.

class Bus(Vehicle): #Родительский класс помещается в скобки 
    def __init__(self, max_speed, mileage, capacity, name): #вызваем метод инициализации родителя
        super().__init__(self, max_speed, mileage, capacity, name) #при помощи функции super()
        
                
#3
#Для класса Bus изменить поведение метода set_name, так чтобы в начало имени автоматически добавлялось "[Bus]". 
#Напрямую к атрибутам Vehicle обращаться нельзя, только через методы класса!

    def set_name(self, name):
        self.name = '[Bus]' + name
        
        
#4 
#Реализовать метод __str__(красивый вывод в строку) и __len__(должен возвращать вместимость транспортного средства)

    def __str__(self):
        return '[скорость-{} пробег-{} места-{} имя-{}]'.format(self.max_speed, self.mileage, self.capacity, self.name)
    def __len__(self):
        pass
