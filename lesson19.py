# ДЗ 4

word = 'helloword'

if word.__contains__(" "):
    print(word.upper()) # Возвращает строку в верхнем регистре
else:
    print(word.lower())
# Второй способ

if ' ' in word:
    word = word.upper()
else:
    word = word.lower()
print(word)