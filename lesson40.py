# lambda выражения
# Когда нужна функция в качестве аргумента и она размером в 1 строчку

def get_square(num):
    print(num ** 2) # Вторая степень

print(get_square(5))

# Использование лямбды
print((lambda num: num ** 2)(10))
