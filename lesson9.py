# Форматирование строк
name = "Hisoka"
age = 25
print("My name is %(name)s. I\'m %(age)d" %
      {'name': name, 'age': age})  # Старый вариант редактирования строк!
# Второй вариант старой записи! %f дробные %.2f
print("My name is %s. I\'m %d" % (name, age))

# Format второй способ.
print("My name is {}. I\'m {}".format(name, age))
print("My name is {1}. I\'m {0}".format(name, age))  # явное использование
# или
print("My name is {name}. I\'m {age}".format(name="Андрей", age=age))

# f-strings Еще один новый способ)))0)

print(f'My name is {name}. I\'m {age}')

print(f'5 + 2 = {5 + 2}')