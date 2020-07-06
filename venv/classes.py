# Конструктор класса
class Person:


    # Конструктор класса
    # Передаем в конструктор класса переменную name
    def __init__(self, name, age):
        self.name = name
        self._secretName = "Gilgamesh" # Защищаем код, указав перед переменной подчеркивание на уровне указании.
        # Можно изменить или вызвать указав ту же _
        self.__secretCode = "404" # Создание приватной переменной  двумя подчеркиваниями. Менять и выводить мы не можем.
        self.__age = 21
    # Еще существует деструктор

    def getSecretCode(self): # Геттер
        return self.__secretCode

    def setSecretCode(self, code): # Сеттер
        self.__secretCode = code

    def info(self):
        print("Current name is " + self.name)

    @property # Используем декоратор для создания Геттера
    def age(self): # Должны идти по парядку и называться одинакого
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value


class Employee(Person):
    def __init__(self, name, age, company): # Конструкторы в Питоне можно перегружать
        super().__init__(name,age) # Обращаемся в метод родительского супер класса и отдаем два параметра
        self.company = company






