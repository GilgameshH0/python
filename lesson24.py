# Словарь - неупорядочная коллекция с доступом по ключу - ассоциативная массивы - хеш таблицы
d = {} # Пустой словарь
product = {
    'title': 'Sony',
    'price': 100
}
product2 = dict(title='iPhone', price=110)
print(product2)
# Создание словаря из списка или кортежа
users = [
    ['oleg@gmail.com', 'Oleg'],
    ['arina@yandex.ru', 'Arina'],
    ['John@mail.ru', 'John']
]
d_users = dict(users)
print(d_users)
users_t = ( # Тут с кортежем
    ('oleg@gmail.com', 'Oleg'),
    ('arina@yandex.ru', 'Arina'),
    ('John@mail.ru', 'John')
)
dd_users = dict(users_t)
print(dd_users)

product3 = dict.fromkeys(['price1', 'price2', 'price3']) # Еще один способ создания словарей
print(product3)

nums = {i: i + 1 for i in range(1,10)}
print(nums[1]) # так как это число а не строка

# Получаем значение по ключу в словаре
print(product['title'])
# Если ключа не существует, тогда выдаст ошибку
print(product.get('lol', 'No')) # так выдаст None Либо слово которое указано вторым параметром

for key in product:
    print(f'{key}: {product[key]}') # Выводит значения print(product.items)

for key, value in product.items():
    print(key, value) # 

products = [ # Список словарей
    {'title': 'Sony', 'price': 100},
    {'title': 'iPhone', 'price': 200},
    {'title': 'Samsung', 'price': 150}
]
print(products)

for prd in products: # Пробежаться циклом по списку словарей
    print(prd['title'], prd['price'])