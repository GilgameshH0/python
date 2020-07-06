# Основы ООП

class A:
    name = 'Secret body'

    def sayHello(self, name=''):
        if name: # Если Имя передано в качестве аргумента
            return "Hello my friend, " + name + "!"
        else:
            return self.name

myClass = A()
print(myClass.sayHello())