# ДЗ выполнено
WHOAMI = 34
x = 0
k = 0
print('Пожалуйста, угадайте число', end=' ')
while x != WHOAMI:
    x = int(input())
    if WHOAMI != x:
        if x > WHOAMI:
            print('Ваше число больше искомого, попробуйте еще раз', end=' ')
        else:
            print('Ваше число меньше искомого, попробуйте еще раз', end=' ')
    k += 1
print(f"Вы угадали число с {k} попытки")