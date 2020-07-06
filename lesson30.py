# Работа с файлами
# r для чтения
# w для записи, если файл существует то он будет очищен
# a для добавления в конец
# + чтение + запись

f = open('test.txt', 'a', encoding='utf-8') # Создаем ссылку на файл. Указываем путь к файлу, режим работы и кодировку
# text = f.read(1) # Указатель смещается
# text = f.read(2) # читает уже не с 1 символа так как указатель сместился
f.write('Новая строка\n') # записывать
f.close()
#print(text)

lines = ["Первая строка", "Вторая строка"]
# d = open('test.txt', 'a', encoding='utf-8')
# for i in lines:
#     d.write(i + "\n") # записывает элементы списка в файл
# d.close()

# Запись в файл по строкам с помощью метода writelines

o = open('test.txt', 'a', encoding='utf-8')
# o.writelines(lines) # Записывает в одну строку
o.writelines(f'{i}\n' for i in lines) # Записывает построчно каждый элемент      # лучше использовать readlines чтобы не занимать много памяти
o.close()

g = open('test.txt', 'r', encoding='utf-8')
for line in g:
    print(line, end='') # Печатаем каждую строку или line.replace('\n', '')
g.close()

