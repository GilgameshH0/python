# Функции
# Функции всегда неявно возвращают None
def myFunc(s = 'def'):
    print(s)
myFunc("qw")

def get_summ(a, b, c=0, d=1):
    return a + b
#print(get_summ(2, 3, 4, 5))

# Именнованые аргументы можно указывать при вызове, чтобы указать какое число что, но они должны идти после обычных аргументов
# И им должно заранее быть присвоено значение по умолчанию
print(get_summ(3, 2, d = 2))

# Функции с произвольным количеством аргументов
#def get_my(*args, **kargs): #Одна звезда в кортеж # А две - в словарь
def my_foo(*args):
    return sum(args) # Встроенная в питон функция суммы

print(my_foo(3, 5, 10))

def mf(**kwargs):
    print(kwargs)
mf(a=1,b=2,c=20) # Выведет ключ со значением Также и со словарями

def f(a,x, *args, ** kwargs):
    print(a)
    print(x)
    print(args)
    print(kwargs)

f(1,2,3,4,b='test',c='heh')

# Документирование функции
def foo(a, b):
    """
    Складывает два числа.

    :param a: Первый операнд
    """
    return a + b
print(foo(1,2))

#Ключевое слово global
acs = 5
def fr():
    global acs
    acs +=1
fr()
print(acs)

l = [1,2,3]
def ferd(l):
    return [i*2 for i in l]
print(ferd(l))