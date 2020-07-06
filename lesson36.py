# Инкапсуляция

from classes import *

man = Person("Oleg")

man.setSecretCode("101")
print(man.getSecretCode())

man.age = 210 # Также без скобок
print(man.age) # Вызываем Геттер age без ()