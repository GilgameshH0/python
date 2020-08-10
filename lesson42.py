# Tkinter

from tkinter import *

root = Tk() # Создаем объект Tkinter
root.title('GUi app')
root.geometry('600x400') # Размер
root.resizable(False, False) # Запрещаем изменять размер окна
root.config(bg='#000') # Цвет фона
root.mainloop() # Метод который будет работать в фоне и реагировать на события



